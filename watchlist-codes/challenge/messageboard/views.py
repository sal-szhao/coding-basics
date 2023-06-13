from flask import render_template, request, url_for, redirect, flash

from messageboard import app, db
from messageboard.models import Message
from messageboard.forms import MessageForm


@app.route('/', methods=['GET', 'POST'])
def index():
    form = MessageForm()
    if form.validate_on_submit():
        name = form.name.data
        message = form.message.data
        
        message = Message(name=name, message=message)
        db.session.add(message)
        db.session.commit()
        flash('Your message have been sent to the world!')
        return redirect(url_for('index'))


    messages = Message.query.order_by(Message.time.desc()).all()
    return render_template('index.html', messages=messages, form=form)





