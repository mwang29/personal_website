from flask import Flask, render_template, url_for, flash, request
from forms import CreditCardForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '1781a2dc5ae8f2ad5e941dbe90d58b8e'

posts = [
    {
        'title': 'My first website!',
        'content': 'Content goes here',
        'date_posted': 'March 14, 2020'
    },
]


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html', title="About")


@app.route('/blog')
def blog():
    return render_template('blog.html', title="Blog", posts=posts)


@app.route('/resume')
def resume():
    return render_template('resume.html', title="Resume")


@app.route('/projects')
def projects():
    return render_template('index.html', title="Projects")


@app.route('/contact')
def contact():
    return render_template('contact.html', title="Contact")


@app.route('/cashback', methods=['GET', 'POST'])
def cashback():
    best_cards, select_cat, member_rec, card_names, cat_card_dict, mult = None, {
    }, {}, None, None, None
    form = CreditCardForm()
    if form.validate_on_submit():
        best_cards, select_cat, member_rec, card_names, mult = form.calculate_cb()
    return render_template('cashback.html', title='Cash Back Calculator', form=form,
                           best_cards=best_cards, select_cat=select_cat, member_rec=member_rec,
                           card_names=card_names, mult=mult)


if __name__ == '__main__':
    app.run(debug=True)
