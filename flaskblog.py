'''
Main flask script for website. Includes routes for all
webpages and runs the app itself.

Made by Michael Wang, 2020
'''

from flask import Flask, render_template
from forms import CreditCardForm
from static.cc_urls import *

app = Flask(__name__)

app.config['SECRET_KEY'] = '1781a2dc5ae8f2ad5e941dbe90d58b8e'


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html', title="About")


@app.route('/blog')
def blog():
    return render_template('blog.html', title="Blog")


@app.route('/resume')
def resume():
    return render_template('resume.html', title="Resume")


@app.route('/projects')
def projects():
    return render_template('index.html', title="Projects")


@app.route('/contact')
def contact():
    return render_template('contact.html', title="Contact")


@app.route('/epidemic/epidemic')
def epidemic():
    return render_template('epidemic.html', title="Epidemic")


@app.route('/epidemic/aboutus')
def aboutus():
    return render_template('aboutus.html', title="aboutus")


@app.route('/epidemic/demographics')
def demographics():
    return render_template('demographics.html', title="demographics")


@app.route('/epidemic/contact2')
def contact2():
    return render_template('contact2.html', title="contact2")


@app.route('/epidemic/policies')
def policies():
    return render_template('policies.html', title="policies")


@app.route('/epidemic/simulator')
def simulator():
    return render_template('simulator.html', title="simulator")


@app.route('/cashback', methods=['GET', 'POST'])
def cashback():
    form = CreditCardForm()
    if form.validate_on_submit():
        results = form.calculate_cb()
        return render_template('cashback.html', title='Cash Back Calculator',
                               form=form, **results, cc_urls=cc_urls)
    else:
        return render_template('cashback.html', title='Cash Back Calculator',
                               form=form, best_combo=None)


if __name__ == '__main__':
    app.run(debug=True)
