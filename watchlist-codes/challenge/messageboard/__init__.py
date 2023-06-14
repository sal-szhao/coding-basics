import os
import sys

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from flask_bootstrap import Bootstrap5
from flask_moment import Moment

app = Flask(__name__)
app.config.from_pyfile('settings.py')

db = SQLAlchemy(app)
bootstrap = Bootstrap5(app)
moment = Moment(app)

# Models and forms don't need initialization.
from messageboard import views, errors, commands
