from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, Email

import os


app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev')

bootstrap = Bootstrap(app)


class LoginForm(FlaskForm):
    email = StringField(u'邮箱', validators=[
                DataRequired(message= u'邮箱不能为空'), 
                Length(1, 64),
                Email(message= u'请输入有效的邮箱地址, 比如:username@domain.com')])
    password = PasswordField(u'密码', validators=[  
                DataRequired(message= u'密码不能为空'),
                Length(5, 18)])
    submit = SubmitField(u'登录')


@app.route('/')
def hello():
    return 'Hello'


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return 'success'
    
    return render_template('login.html', form=form)
