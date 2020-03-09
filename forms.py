import numpy as np
from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField, SelectField
from wtforms.validators import DataRequired, InputRequired
from cb.cashback import process_data, calc_cb, calc_stats


class CreditCardForm(FlaskForm):
    total_spend = IntegerField(
        'Total Monthly Spend', validators=[DataRequired()])  # required field
    groceries = IntegerField('Groceries', validators=[DataRequired()])
    gas = IntegerField('Gas', validators=[DataRequired()])
    restaurants = IntegerField('Restaurants', validators=[DataRequired()])
    entertainment = IntegerField('Entertainment', validators=[DataRequired()])
    travel = IntegerField('Travel', validators=[DataRequired()])
    cell_carrier = IntegerField(
        'Cell Phone Carrier', validators=[DataRequired()])
    gym = IntegerField('Gym/Fitness Memberships', validators=[DataRequired()])
    online_shopping = IntegerField(
        'Online Shopping, not including Amazon', validators=[DataRequired()])
    amazon = IntegerField('Amazon', validators=[DataRequired()])
    home_improvement = IntegerField(
        'Home Improvement', validators=[DataRequired()])
    internet = IntegerField(
        'Internet, Cable, Streaming Services', validators=[DataRequired()])
    sporting_goods = IntegerField(
        'Sporting Good Stores', validators=[DataRequired()])
    apple = IntegerField('Apple Store', validators=[DataRequired()])
    foreign_transaction = IntegerField(
        'Foreign Transactions', validators=[DataRequired()])
    rideshare = IntegerField('Rideshares (Uber/Lyft)',
                             validators=[DataRequired()])
    num_cards = IntegerField('How many credit cards do you prefer?',
                             validators=[InputRequired()])
    amazon_member = SelectField('Are you an Amazon member?',
                                choices=[(True, 'Yes'), (False, 'No')],
                                validators=[InputRequired()])
    costco_member = SelectField("Are you a Costco member?",
                                choices=[(True, 'Yes'), (False, 'No')],
                                validators=[InputRequired()])
    sams_member = SelectField("Are you a Sam's Club member?",
                              choices=[(True, 'Yes'), (False, 'No')],
                              validators=[InputRequired()])
    boa_amt = IntegerField(
        'Capital in existing Bank of America accounts (optional):', default=0)
    submit = SubmitField('Calculate!')

    def calculate_cb(self):
        total_spend = self.total_spend.data
        spend = np.array([self.groceries.data, self.gas.data,
                          self.restaurants.data, self.entertainment.data, self.travel.data,
                          self.cell_carrier.data, self.gym.data, self.online_shopping.data,
                          self.amazon.data, self.home_improvement.data,
                          self.internet.data, self.sporting_goods.data, self.apple.data,
                          self.foreign_transaction.data, self.rideshare.data,
                          max(total_spend - sum(spend), 0)])  # etc etc
        attr = {'amazon_member': self.amazon_member.data, 'costo_member': self.costco_member.data,
                'sams_member': self.sams_member.data]  # etc etc
        comb_dict, card_vectors, card_names = process_data()
        num_cards = self.num_cards.data
        max_cb, best_combo, member, select_cat = calc_cb(
            comb_dict, num_cards, card_vectors, spend, attr)
        avg_cb, annual_cb = calc_stats(spend, max_cb)
        return best_combo
