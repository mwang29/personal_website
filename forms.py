import numpy as np
from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField, SelectField
from wtforms.validators import DataRequired, InputRequired, NumberRange
from cb.cashback import process_data, calc_cb, calc_stats


class CreditCardForm(FlaskForm):
    total_spend = IntegerField('Total Monthly Spend',
                               validators=[DataRequired()])  # required field
    groceries = IntegerField('Groceries',
                             validators=[DataRequired()])
    gas = IntegerField('Gas',
                       validators=[DataRequired()])
    restaurants = IntegerField('Restaurants',
                               validators=[DataRequired()])
    entertainment = IntegerField('Entertainment',
                                 validators=[DataRequired()])
    travel = IntegerField('Travel',
                          validators=[DataRequired()])
    utilities = IntegerField('Utilities',
                             validators=[DataRequired()])
    cell_carrier = IntegerField('Cell Phone Carrier',
                                validators=[DataRequired()])
    gym = IntegerField('Gym/Fitness Memberships',
                       validators=[DataRequired()])
    online_shopping = IntegerField('Online Shopping, not including Amazon',
                                   validators=[DataRequired()])
    amazon = IntegerField('Amazon',
                          validators=[DataRequired()])
    home_improvement = IntegerField('Home Improvement',
                                    validators=[DataRequired()])
    internet = IntegerField('Internet, Cable, Streaming Services',
                            validators=[DataRequired()])
    sporting_goods = IntegerField('Sporting Good Stores',
                                  validators=[DataRequired()])
    apple = IntegerField('Apple Store',
                         validators=[DataRequired()])
    foreign_transaction = IntegerField('Foreign Transactions',
                                       validators=[DataRequired()])
    rideshare = IntegerField('Rideshares (Uber/Lyft)',
                             validators=[DataRequired()])
    num_cards = IntegerField('How many credit cards do you prefer? (1-6)',
                             validators=[InputRequired(),
                                         NumberRange(min=1, max=6,
                                                     message="Please enter a number between 1 and 6")])
    amazon_member = SelectField('Are you an Amazon member?',
                                choices=[(True, 'Yes'), (False, 'No')],
                                validators=[InputRequired()])
    costco_member = SelectField("Are you a Costco member?",
                                choices=[(True, 'Yes'), (False, 'No')],
                                validators=[InputRequired()])
    sams_member = SelectField("Are you a Sam's Club member?",
                              choices=[(True, 'Yes'), (False, 'No')],
                              validators=[InputRequired()])
    boa_amt = IntegerField('Capital in existing Bank of America accounts (optional):',
                           default=0)

    submit = SubmitField('Calculate!')

    def calculate_cb(self):
        num_cards = self.num_cards.data
        boa_multiplier = self.get_boa_multiplier()
        spend, attr = self.get_spend_attr()
        comb_dict, card_vectors, card_names = process_data(boa_multiplier)
        max_cb, best_combo, member, select_cat = calc_cb(
            comb_dict, num_cards, card_vectors, card_names, spend, attr)
        avg_cb, annual_cb = calc_stats(spend, max_cb)
        best_cards = self.get_best_cards(card_names, best_combo)
        return best_cards, select_cat

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
        spend = [self.groceries.data, self.gas.data,
                 self.restaurants.data, self.entertainment.data,
                 self.travel.data, self.utilities.data,
                 self.cell_carrier.data, self.gym.data,
                 self.online_shopping.data, self.amazon.data,
                 self.home_improvement.data, self.internet.data,
                 self.sporting_goods.data, self.apple.data,
                 self.foreign_transaction.data, self.rideshare.data]

        other = max(total_spend - sum(spend), 0)
        spend.append(other)
        spend = np.array(spend)

        attr = {'amazon_member': self.amazon_member.data,
                'costco_member': self.costco_member.data,
                'sams_member': self.sams_member.data}

        return spend, attr

    @staticmethod
    def get_best_cards(card_names, best_combo):
        best_cards = []
        cards = [card_names[i] for i in best_combo]
        for card in cards:
            best_cards.append(card)
        return best_cards
