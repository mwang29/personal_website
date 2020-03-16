'''
Handles all forms on personal website. Includes cash back calculator form
and its methods for returning information to the html file.

Made by Michael Wang in 2020.
'''

import numpy as np
from flask_wtf import FlaskForm
from wtforms import DecimalField, IntegerField, SubmitField, BooleanField
from wtforms.validators import InputRequired, NumberRange, Optional
from cb.cashback import process_data, calc_cb, calc_stats


class CreditCardForm(FlaskForm):
    '''
    Class for accepting user input, processing the input, and passing the
    output to html to show user results
    '''
    prompt = "Please enter a number between 1 and 8"
    total = DecimalField('Total Monthly Spend',
                         validators=[Optional()],
                         render_kw={"placeholder": "0"})  # required field
    groceries = DecimalField('Groceries', validators=[Optional()],
                             render_kw={"placeholder": "0"})
    gas = DecimalField('Gas', validators=[Optional()],
                       render_kw={"placeholder": "0"})
    restaurants = DecimalField('Restaurants', validators=[Optional()],
                               render_kw={"placeholder": "0"})
    entertainment = DecimalField('Entertainment',
                                 validators=[Optional()],
                                 render_kw={"placeholder": "0"})
    travel = DecimalField('Travel', validators=[Optional()],
                          render_kw={"placeholder": "0"})
    utilities = DecimalField('Utilities', validators=[Optional()],
                             render_kw={"placeholder": "0"})
    cell_carrier = DecimalField('Cell Phone Carrier', validators=[Optional()],
                                render_kw={"placeholder": "0"})
    gym = DecimalField('Gym/Fitness Memberships', validators=[Optional()],
                       render_kw={
                       "placeholder": "0"})
    online_shopping = DecimalField('Online Shopping, not including Amazon',
                                   validators=[Optional()],
                                   render_kw={"placeholder": "0"})
    amazon = DecimalField('Amazon', validators=[Optional()],
                          render_kw={"placeholder": "0"})
    home_improvement = DecimalField('Home Improvement',
                                    validators=[Optional()],
                                    render_kw={"placeholder": "0"})
    internet = DecimalField('Internet, Cable, Streaming Services',
                            validators=[Optional()],
                            render_kw={"placeholder": "0"})
    sporting_goods = DecimalField('Sporting Good Stores',
                                  validators=[Optional()],
                                  render_kw={"placeholder": "0"})
    apple = DecimalField('Apple Store', validators=[Optional()],
                         render_kw={"placeholder": "0"})
    foreign_transaction = DecimalField('Foreign Transactions',
                                       validators=[Optional()],
                                       render_kw={"placeholder": "0"})
    rideshare = DecimalField('Rideshares (Uber/Lyft)', validators=[Optional()],
                             render_kw={"placeholder": "0"})
    num_cards = IntegerField('How many credit cards? (1-8)',
                             validators=[InputRequired(),
                                         NumberRange(min=1, max=8,
                                                     message=prompt)],
                             default=2)
    amazon_member = BooleanField('Amazon Member:')
    costco_member = BooleanField('Costco Member:')
    sams_member = BooleanField("Sam's Club Member:")
    boa_amt = DecimalField('Capital in existing Bank of America accounts',
                           validators=[Optional()],
                           render_kw={"placeholder": "0"})

    submit = SubmitField('Calculate!')

    def calculate_cb(self):
        '''
        Calls other methods to calculate cash back and
        returns all necessary output in a dictionary
        '''
        num_cards = self.num_cards.data
        boa_multiplier = self.get_boa_multiplier()
        spend, attr = self.get_spend_attr()
        comb_dict, card_vectors, card_names = process_data(boa_multiplier)
        max_cb, best_combo, member_rec, select_cat = calc_cb(
            comb_dict, num_cards, card_vectors, card_names, spend, attr)
        avg_cb, annual_cb = calc_stats(spend, max_cb)
        results = {'best_combo': best_combo, 'select_cat': select_cat,
                   'member_rec': member_rec, 'card_names': card_names,
                   'mult': boa_multiplier, 'avg_cb': avg_cb,
                   'annual_cb': annual_cb}
        return results

    def get_boa_multiplier(self):
        '''
        Depending on capital in existing BOA accounts, the user
        qualifies for a rewards level that increases cash back.
        This function decides the multiplier used in the calculation.
        '''
        boa_multiplier = 1
        if self.boa_amt.data is None:
            self.boa_amt.data = 0
        if self.boa_amt.data >= 100000:
            boa_multiplier = 1.75
        elif self.boa_amt.data >= 50000:
            boa_multiplier = 1.5
        elif self.boa_amt.data >= 20000:
            boa_multiplier = 1.25
        return boa_multiplier

    def get_spend_attr(self):
        '''
        Compiles completed form into a spend array used in calculations
        for cash back. Also keeps track of whether or not members
        '''
        if self.total.data is None:
            total_spend = 0
        else:
            total_spend = self.total.data
        temp_spend = [self.groceries.data, self.gas.data,
                      self.restaurants.data, self.entertainment.data,
                      self.travel.data, self.utilities.data,
                      self.cell_carrier.data, self.gym.data,
                      self.online_shopping.data, self.amazon.data,
                      self.home_improvement.data, self.internet.data,
                      self.sporting_goods.data, self.apple.data,
                      self.foreign_transaction.data, self.rideshare.data]
        temp_spend = [0 if v is None else v for v in temp_spend]
        other = max(total_spend - sum(temp_spend), 0)
        temp_spend.append(other)
        spend = [float(i) for i in temp_spend]
        spend = np.array(spend)

        attr = {'amazon_member': self.amazon_member.data,
                'costco_member': self.costco_member.data,
                'sams_member': self.sams_member.data}

        return spend, attr
