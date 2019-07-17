from app import app
from flask import render_template, url_for, redirect
from app.forms import TitleForm, ContactForm, LoginForm, RegisterForm, PostForm

@app.route('/')
@app.route('/index')
@app.route('/index/<header>', methods=['GET'])
def index(header=''):
    products = [
        {
            'id': 1001,
            'title': 'Soap',
            'price': '3.98',
            'desc': 'Very clean soapy soap. Has soapness.'
        },
        {
            'id': 1002,
            'title': 'Grapes',
            'price': '4.55',
            'desc': 'This is a bundle of grapey grapes.'
        },
        {
            'id': 1003,
            'title': 'Laptop',
            'price': '1100.99',
            'desc': 'Great for laps and tops.'
        },
        {
            'id': 1004,
            'title': 'Chair',
            'price': '114.45',
            'desc': 'Great for sitting and standing on.'
        }
    ]
    return render_template('index.html', title='Home', products=products, header=header)

@app.route('/checkout')
def checkout():
    return render_template('checkout.html', title='Checkout')

@app.route('/title', methods=['GET', 'POST'])
def title():
    # create an instance of the form
    form = TitleForm()

    # write a conditional that checks if form was submitted properly
    if form.validate_on_submit():
        return redirect(url_for('index', header=form.title.data))

    return render_template('form.html', form=form, title='Change Title')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        # TODO: setup Placeholder
        pass

    return render_template('form.html', form=form, title='Login')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        # TODO: setup Placeholder
        pass

    return render_template('form.html', form=form, title='Register')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()

    if form.validate_on_submit():
        # TODO: setup Placeholder
        pass


    return render_template('form.html', form=form, title='Contact Us')

# temp variable for testing
posts = [
    {
        'post_id': 1,
        'tweet': 'My favorite suit is spades.',
        'date_posted': '7/17/2019'
    },
    {
        'post_id': 2,
        'tweet': 'My favorite color is green.',
        'date_posted': '7/10/2019'
    },
    {
        'post_id': 3,
        'tweet': 'My favorite drink is coffee.',
        'date_posted': '7/1/2019'
    },\
]
@app.route('/profile', methods=['GET', 'POST'])
def profile():
    form = PostForm()

    if form.validate_on_submit():
        posts.append(
            {
                'post_id': len(posts) + 1,
                'tweet': form.tweet.data,
                'date_posted': '7/17/2019'
            }
        )

        return redirect(url_for('profile'))
    return render_template('profile.html', form=form, title='Profile', posts=posts)
