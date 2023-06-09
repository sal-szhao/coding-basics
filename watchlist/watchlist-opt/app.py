import os
import sys

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

import click


app = Flask(__name__)

@app.context_processor
def inject_user():
    user = User.query.first()
    return dict(user=user)
    

@app.route('/')
def index():
    movies = Movie.query.all()
    return render_template('index.html', movies=movies)


# Create database models
WIN = sys.platform.startswith('win')
if WIN:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'

app.config['SQLALCHEMY_DATABASE_URI'] = prefix + os.path.join(app.root_path, 'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60))
    year = db.Column(db.String(4))


@app.cli.command()
@click.option('--drop', is_flag=True, help='Create after drop.')
def initdb(drop):
    if drop: db.drop_all()
    db.create_all()
    click.echo('Initialized database.')

@app.cli.command()
def forge():
    db.create_all()

    # Insertion of database.
    user = User(name=name)
    db.session.add(user)
    for m in movies:
        movie = Movie(title=m['title'], year=m['year'])
        db.session.add(movie)

    db.session.commit()
    click.echo('Done.')

# user variable in context_processor will be automatically loaded when template rendering.
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
    
