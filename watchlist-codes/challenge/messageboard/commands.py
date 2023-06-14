import click

from messageboard import app, db
from messageboard.models import Message

@app.cli.command()
@click.option('--drop', is_flag=True, help='Create after drop.')
def initdb(drop):
    if drop: db.drop_all()
    db.create_all()
    click.echo('Initialized database.')


@app.cli.command()
@click.option('--count', default=20, help='Quantity of the fake messages, 20 by default.')
def forge(count):
    db.drop_all()
    db.create_all()

    from faker import Faker
    
    fake = Faker()
    for i in range(count):
        message = Message(
            name=fake.name(), 
            message=fake.sentence(), 
            time=fake.date_time_this_year()
        )
        db.session.add(message)
    
    db.session.commit()
    click.echo('Created {} faked messages.'.format(count))