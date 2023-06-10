from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello'

# Add html code to the return.
@app.route('/index')
@app.route('/home')
def helloTotoro():
    return '<h1>Hello Totoro!</h1><img src="http://helloflask.com/totoro.gif">'


# Variable in url can serve as input.
from markupsafe import escape

@app.route('/user/<string:name>')
def user_page(name):
    return f'User: {escape(name)}'

# Generate url automatically from view functions.
@app.route('/test')
def test_url_for():
    print(url_for('hello'))
    print(url_for('user_page', name='greyli'))
    print(url_for('user_page', name='peter'))
    print(url_for('test_url_for'))
    ## Additional keyword will be treated as query strings appended to the url.
    print(url_for('test_url_for', num=2))  # output：/test?num=2
    return 'Test page'
