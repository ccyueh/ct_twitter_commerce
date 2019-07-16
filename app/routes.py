from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
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
    return render_template('index.html', title='Home', products=products)

@app.route('/checkout')
def checkout():
    return render_template('checkout.html', title='Checkout')

@app.route('/title')
def title():
    return render_template('title.html', title='Change Title')
