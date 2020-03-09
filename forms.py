import numpy as np
from flask_wtf import FlaskForm
from wtforms import DecimalField, IntegerField, SubmitField, SelectField, BooleanField
from wtforms.validators import InputRequired, NumberRange
from cb.cashback import process_data, calc_cb, calc_stats


class CreditCardForm(FlaskForm):
    total_spend = DecimalField('Total Monthly Spend', places=2, rounding=None,
                               validators=[InputRequired()], default=0)  # required field
    groceries = DecimalField('Groceries',
                             validators=[InputRequired()], default=0)
    gas = DecimalField('Gas',
                       validators=[InputRequired()], default=0)
    restaurants = DecimalField('Restaurants',
                               validators=[InputRequired()], default=0)
    entertainment = DecimalField('Entertainment',
                                 validators=[InputRequired()], default=0)
    travel = DecimalField('Travel',
                          validators=[InputRequired()], default=0)
    utilities = DecimalField('Utilities',
                             validators=[InputRequired()], default=0)
    cell_carrier = DecimalField('Cell Phone Carrier',
                                validators=[InputRequired()], default=0)
    gym = DecimalField('Gym/Fitness Memberships',
                       validators=[InputRequired()], default=0)
    online_shopping = DecimalField('Online Shopping, not including Amazon',
                                   validators=[InputRequired()], default=0)
    amazon = DecimalField('Amazon',
                          validators=[InputRequired()], default=0)
    home_improvement = DecimalField('Home Improvement',
                                    validators=[InputRequired()], default=0)
    internet = DecimalField('Internet, Cable, Streaming Services',
                            validators=[InputRequired()], default=0)
    sporting_goods = DecimalField('Sporting Good Stores',
                                  validators=[InputRequired()], default=0)
    apple = DecimalField('Apple Store',
                         validators=[InputRequired()], default=0)
    foreign_transaction = DecimalField('Foreign Transactions',
                                       validators=[InputRequired()], default=0)
    rideshare = DecimalField('Rideshares (Uber/Lyft)',
                             validators=[InputRequired()], default=0)
    num_cards = IntegerField('How many credit cards do you prefer? (1-8)',
                             validators=[InputRequired(),
                                         NumberRange(min=1, max=8,
                                                     message="Please enter a number between 1 and 6")],
                             default=2)
    amazon_member = BooleanField('Amazon Member:')
    costco_member = BooleanField('Costco Member:')
    sams_member = BooleanField("Sam's Club Member:")
    boa_amt = DecimalField('Capital in existing Bank of America accounts (optional):',
                           default=0)

    submit = SubmitField('Calculate!')

    def calculate_cb(self):
        num_cards = self.num_cards.data
        boa_multiplier = self.get_boa_multiplier()
        spend, attr = self.get_spend_attr()
        comb_dict, card_vectors, card_names = process_data(boa_multiplier)
        max_cb, best_combo, member_rec, select_cat = calc_cb(
            comb_dict, num_cards, card_vectors, card_names, spend, attr)
        avg_cb, annual_cb = calc_stats(spend, max_cb)
        best_cards = self.get_best_cards(card_names, best_combo)
        return best_cards, select_cat, member_rec

    def get_boa_multiplier(self):
        boa_multiplier = 1
        if self.boa_amt.data >= 100000:
            boa_multiplier = 1.75
        elif self.boa_amt.data >= 50000:
            boa_multiplier = 1.5
        elif self.boa_amt.data >= 20000:
            boa_multiplier = 1.25
        return boa_multiplier

    def get_spend_attr(self):
        total_spend = self.total_spend.data
        temp_spend = [self.groceries.data, self.gas.data,
                      self.restaurants.data, self.entertainment.data,
                      self.travel.data, self.utilities.data,
                      self.cell_carrier.data, self.gym.data,
                      self.online_shopping.data, self.amazon.data,
                      self.home_improvement.data, self.internet.data,
                      self.sporting_goods.data, self.apple.data,
                      self.foreign_transaction.data, self.rideshare.data]
        other = max(total_spend - sum(temp_spend), 0)
        temp_spend.append(other)
        spend = [int(i) for i in temp_spend]
        spend = np.array(spend)

        attr = {'amazon_member': self.amazon_member.data,
                'costco_member': self.costco_member.data,
                'sams_member': self.sams_member.data}

        return spend, attr

    @staticmethod
    def get_best_cards(card_names, best_combo):
        best_cards = []
        if best_combo:
            cards = [card_names[i] for i in best_combo]
            for card in cards:
                best_cards.append(card)
        else:
            best_cards = ['Citi Double Cash Card']
        return best_cards
