from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError

def command_check(form, field):
    if field.data != u'宝塔镇河妖':
        raise ValidationError('The captcha value must be "宝塔镇河妖".')
        
class MessageForm(FlaskForm):
    name = StringField('Name', validators=[
                DataRequired(), 
                Length(1, 20)])
    message = TextAreaField('Message', validators=[  
                DataRequired(),
                Length(1, 200)])
    password = StringField(u'天王盖地虎', validators=[  
                DataRequired(),
                command_check])
    submit = SubmitField('Submit')
