'''
Python backend for calculating cash back. Can operate as a script by itself
without using flask app by running 'python cashback.py'

Made by Michael Wang in 2020
'''

import pandas as pd
import numpy as np
from itertools import combinations, product


def process_data(boa_multiplier):
    '''Processes csv file based on boa multiplier and returns
    intermediate logical dictionary 'comb_dict' to work with US bank
    and BOA cards (assigning all combinations of choices to one card)
    , a pandas dataframe 'card_vectors' that gives all rows of each
    possible card's rewards, and 'card_names' which is a list of the
    card names for all card rewards.
    '''
    data = pd.read_csv('card_data.csv')
    categories = list(data.columns)[2:]
    card_names = list(data.Card_Name)
    card_vectors = data[categories]

    us_bank_cats = card_vectors.loc[0, card_vectors.columns !=
                                    'Foreign_Transactions']
    us_bank_cats = us_bank_cats.to_numpy().nonzero()[0]
    us_bank_combinations = combinations(us_bank_cats, 2)
    boa_cats = card_vectors.loc[4, card_vectors.columns !=
                                'Foreign_Transactions'].to_numpy().nonzero()[0]
    boa_combinations = combinations(boa_cats, 1)

    # intermediate df for for each choice of 2 categories in us bank card
    us_bank_vec = []
    for c in us_bank_combinations:
        temp_row = np.zeros(len(categories))
        temp_row[list(c)] = card_vectors.iloc[0][list(c)]
        us_bank_vec.append(temp_row)
        card_names.append(card_names[0])
    us_bank_df = pd.DataFrame(us_bank_vec, columns=categories)

    # intermediate df for for each choice of 1 category in boa card
    boa_vec = []
    for c in boa_combinations:
        temp_row = np.zeros(len(categories))
        temp_row[list(c)[0]] = card_vectors.iloc[4][list(c)[0]]
        boa_vec.append(temp_row)
        card_names.append(card_names[4])
    boa_df = pd.DataFrame(boa_vec, columns=categories)

    # remove original boa and us bank rows, and remove from card names
    card_vectors = card_vectors.drop(
        index=card_vectors.index[[0, 4]]).reset_index(drop=True)
    del card_names[4]
    del card_names[0]

    # attach intermediate rows
    card_vectors = card_vectors.append(us_bank_df, ignore_index=True)
    boa_df *= boa_multiplier
    card_vectors = card_vectors.append(boa_df, ignore_index=True)

    # assign index of new rows to us bank and boa card names
    comb_dict = {}
    for i in range(0, 15):
        comb_dict[card_names[i]] = [i]
    comb_dict[card_names[15]] = list(range(15, 25))
    comb_dict[card_names[26]] = list(range(25, 29))
    return comb_dict, card_vectors, card_names


def calc_cb(comb_dict, num_cards, card_vectors, card_names, spend, attr):
    '''
    Main function to calculate the best combination of credit cards
    to maximize cash back.

    Params
        comb_dict: dict : mapping of card names to respective row indices
        num_cards: int  : number of cards desired by user
        card_vectors: df: dataframe of cash back percentages for each selection
        card_names: list: list of names for each row in card_vectors
        spend: np array : input spend of each category
        attr: dict      : whether or not user is member of clubs
    '''

    # decide number of cards to guarantee optimization, then use heuristic
    max_cb, best_combo, member_rec, additional_cards = 0, [4], {}, 0
    if num_cards > 3:
        additional_cards = num_cards - 3
        num_cards = 3

    # Iterate through all combinations based on rules set by dictionary
    for comb in combinations(sorted(comb_dict), num_cards):
        for uniquecomb in product(*[comb_dict[i] for i in comb]):
            temp_cb = calc_temp_cb(card_vectors, spend,
                                   uniquecomb, num_cards, attr)
            if temp_cb > max_cb:  # if we find a better combination, then...
                max_cb = temp_cb
                best_combo = uniquecomb
                member_rec = recommend_membership(attr, uniquecomb)

    # If we chose more than 3 cards, use heuristic for the rest
    if additional_cards > 0:
        best_combo = list(best_combo)
        before_cb = max_cb
        all_cards = range(len(comb_dict))
        us_bank = [15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
        boa = [25, 26, 27, 28]
        us_bank_overlap = [i for i in us_bank if i in best_combo]
        boa_overlap = [i for i in boa if i in best_combo]
        if us_bank_overlap:
            all_cards = [i for i in all_cards if i not in us_bank]
        if boa_overlap:
            all_cards = [i for i in all_cards if i not in us_bank]

        # empty list of additional cards we decide to add after 3 optimal
        added_cards = []

        for c in range(additional_cards):  # for each additional card slot
            # only look at non added cards
            us_bank_overlap = [i for i in us_bank if i in added_cards]
            boa_overlap = [i for i in boa if i in added_cards]
            if us_bank_overlap:
                all_cards = [i for i in all_cards if i not in us_bank]
            if boa_overlap:
                all_cards = [i for i in all_cards if i not in boa]
            for new_card in all_cards:  # for all potential cards we can add,
                temp_cb = calc_temp_cb(card_vectors, spend,
                                       best_combo + [new_card],
                                       num_cards, attr)
                if temp_cb > max_cb:  # which is the next card we should add?
                    max_cb = temp_cb
                    best_card = new_card
            if max_cb > before_cb:  # if the card improves our cash back
                best_combo.append(best_card)
                before_cb = max_cb
                added_cards.append(best_card)

    select_cat = {}
    # Which categories of choose cards selected?
    if best_combo:  # if we entered values
        for card in best_combo:
            if card_names[card] == card_names[15]:
                s = card_vectors.iloc[card]
                select_cat['us_bank'] = list(s.axes[0][s > 0])
            if card_names[card] == card_names[25]:
                s = card_vectors.iloc[card]
                select_cat['boa'] = list(s.axes[0][s > 0])
    return max_cb, best_combo, member_rec, select_cat


def calc_stats(spend, max_cb):
    '''
    Simple function to calculate annual and avg cash back
    given our max cash back.
    '''
    avg_cb = max_cb / sum(spend)
    annual_cb = max_cb * 12
    return avg_cb, annual_cb


def calc_temp_cb(card_vectors, spend, uniquecomb, num_cards, attr):
    '''
    For each selection of card combinations, calculates the cash back
    we would get. Handles all card types available.
    '''

    # calculate discover cash back advantage
    # calculate earnings in cats
    if 7 in uniquecomb and num_cards > 1:
        temp_cb = sum(np.multiply(card_vectors.iloc[7, :].to_numpy(),
                                  spend))

        # get non-discover cards in uniquecomb
        other_cards = np.array([card for card in uniquecomb if card != 7])
        # indices of discover categories
        d_ind = np.array(card_vectors.iloc[7, :].to_numpy().nonzero())[0]
        other_cb = sum(np.multiply(card_vectors.iloc[other_cards, d_ind].to_numpy()[0],
                                   spend[d_ind]))
        # discover cash back in cats - other cards in those same cats divided by
        temp_cb = (temp_cb - other_cb) / 4
        all_other_cb = sum(np.multiply(card_vectors.iloc[other_cards, :].to_numpy()[0],
                                       spend))
        temp_cb += all_other_cb  # add net cb to all other cards

    # if discover is our only card
    elif 7 in uniquecomb:
        temp_cb = sum(np.multiply(
            card_vectors.iloc[7, :].to_numpy(), spend)) / 4

    # if discover isn't there
    else:
        best_cb = card_vectors.iloc[list(uniquecomb), :].max(axis=0)
        temp_cb = sum(np.multiply(best_cb, spend))

    # Annual fees subtract from cash back
    if 1 in uniquecomb:
        temp_cb -= float(95) / 12
    if 6 in uniquecomb:
        temp_cb -= float(99) / 12
    if 14 in uniquecomb:
        temp_cb -= float(95) / 12
    # Membership costs
    if 11 in uniquecomb and not attr['sams_member']:
        temp_cb -= float(45) / 12
    if 3 in uniquecomb and not attr['amazon_member']:
        temp_cb -= float(119) / 12
    if 0 in uniquecomb and not attr['costco_member']:
        temp_cb -= float(60) / 12

    return temp_cb


def recommend_membership(attr, uniquecomb):
    member_rec = {}
    if 11 in uniquecomb and not attr['sams_member']:
        # We will recommend getting a sam's membership
        member_rec['SC'] = True
    if 3 in uniquecomb and not attr['amazon_member']:
        # Recommend getting amazon membership
        member_rec['AMZN'] = True
    if 0 in uniquecomb and not attr['costco_member']:
        # Recommend getting costco membership
        member_rec['COSTCO'] = True
    return member_rec


if __name__ == "__main__":
    # Get User Input
    print("Please enter avg. monthly spend for the following categories:\n")
    spend, attr = [], {}  # spend and attributes
    total_spend = int(input("Total monthly credit card bills: $"))
    spend.append(int(input("Groceries: $")))
    spend.append(int(input("Gas: $")))
    spend.append(int(input("Eating out: $")))
    spend.append(int(input("Entertainment : $")))
    spend.append(int(input("Travel: $")))
    spend.append(int(input("Utilities: $")))
    spend.append(int(input("Cell phone carrier: $")))
    spend.append(int(input("Gym/Fitness Memberships: $")))
    spend.append(int(input("Online Shopping (not including Amazon): $")))
    spend.append(int(input("Amazon.com: $")))
    spend.append(int(input("Home Improvement Stores: $")))
    spend.append(int(input("Internet, Cable, and Streaming Services: $")))
    spend.append(int(input("Sporting good stores: $")))
    spend.append(int(input("Apple store: $")))
    spend.append(int(input("Foreign transactions: $")))
    spend.append(int(input("Rideshare (Uber, Lyft): $")))
    spend.append(int(max(total_spend - sum(spend), 0)))  # Other expenses
    spend = np.array(spend)

    attr['amazon_member'] = True if input(
        "Amazon member? Y/N: ").lower() == "y" else False
    attr['costco_member'] = True if input(
        "Costco member? Y/N: ").lower() == "y" else False
    attr['sams_member'] = True if input(
        "Sam's Club member? Y/N: ").lower() == "y" else False
    attr['boa'] = True if input(
        "Existing BoA accounts? Y/N: ").lower() == "y" else False
    if attr['boa']:
        boa_amt = int(
            input("How much capital do you have in existing BoA accounts?: "))
        if boa_amt >= 100000:
            boa_multiplier = 1.75
        elif boa_amt >= 50000:
            boa_multiplier = 1.5
        elif boa_amt >= 20000:
            boa_multiplier = 1.25
    else:
        boa_multiplier = 1

    # Process data and make calculations

    comb_dict, card_vectors, card_names = process_data(boa_multiplier)
    num_cards = int(input("Preferred number of cards?\n"))
    max_cb, best_combo, member, select_cat = calc_cb(
        comb_dict, num_cards, card_vectors, card_names, spend, attr)
    avg_cb, annual_cb = calc_stats(spend, max_cb)

    cards = [card_names[i] for i in best_combo]
    for card in cards:
        print(card)

    print(card_names)

    print(f"\nAvg cash back: {avg_cb:.4f}",
          f"\nAnnual cash back: ${annual_cb:.2f}")
    print(f"Total annual spend: ${12*sum(spend):.2f}")
