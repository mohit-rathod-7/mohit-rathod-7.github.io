# Form imports
from re import search
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import *
from wtforms.validators import InputRequired, Length, Email
from wtforms.fields.html5 import EmailField, DecimalField


# ---------------------------------------------- FORMS --------------------------------------------

class LoginForm(FlaskForm):
    email   =   EmailField('Email : ',   validators=[InputRequired(message='Email is required'),    Length(min=4, max=16, message="User name must be 4 to 16 characters long !!!")])
    # username  = StringField('Username : ',    validators=[InputRequired(message='Username is required'), Length(min=4, max=40, message="User name must be 4 to 16 characters long !!!")])
    password  = PasswordField('Password : ',  validators=[InputRequired(message='Password is required'), Length(min=8, max=80, message="Password must be minimum 8 characters long !!!")])
    # remember  = BooleanField('Stay signed in')


class SignupForm(FlaskForm):
    email    = EmailField('Email : ',   validators=[InputRequired(message='Email is required')])
    password = PasswordField('Password : ', validators=[InputRequired(message='Password is required')])
    