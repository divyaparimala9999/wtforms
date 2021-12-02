from flask_wtf import FlaskForm  
from wtforms import StringField,SubmitField
from wtforms import validators,ValidationError


class ContactForm(FlaskForm):
    name=StringField('UserName')
    submit=SubmitField('Submit')
    