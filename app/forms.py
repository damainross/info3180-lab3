from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired,Email
from wtforms import StringField,TextField
class ContactForm(FlaskForm):
    name = StringField('name',validators=[DataRequired()])
    email    = StringField('email',validators= [DataRequired(),Email()])
    message = TextField('message',validators=[DataRequired()])