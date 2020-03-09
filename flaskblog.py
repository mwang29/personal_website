from flask import Flask, render_template, url_for, flash, request
from forms import CreditCardForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '1781a2dc5ae8f2ad5e941dbe90d58b8e'

posts = [
    {
        'author': 'Michael Wang',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'February 20, 2020'
    },
    {
        'author': 'Elizabeth Wang',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'February 21, 2020'
    }
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
    return render_template('blog.html', title="Blog")


@app.route('/resume')
def resume():
    return render_template('resume.html', title="Resume")


@app.route('/projects')
def projects():
    return render_template('projects.html', title="Projects")


@app.route('/contact')
def contact():
    return render_template('contact.html', title="Contact")


@app.route('/cashback', methods=['GET', 'POST'])
def cashback():
    form = CreditCardForm()
    if request.method == 'POST':
        spend = form.calculate_cb()
    else:
        spend = None
    return render_template('cashback.html', title='Cash Back Calculator', form=form, spend=spend)


if __name__ == '__main__':
    app.run(debug=True)
