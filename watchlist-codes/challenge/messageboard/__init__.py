import os
import sys

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from flask_bootstrap import Bootstrap5
from flask_moment import Moment

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev')

WIN = sys.platform.startswith('win')
if WIN:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'

app.config['SQLALCHEMY_DATABASE_URI'] = prefix + os.path.join(os.path.dirname(app.root_path), os.getenv('DATABASE_FILE', 'data.db'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

db = SQLAlchemy(app)
bootstrap = Bootstrap5(app)
moment = Moment(app)

from messageboard import views, errors, commands, forms
