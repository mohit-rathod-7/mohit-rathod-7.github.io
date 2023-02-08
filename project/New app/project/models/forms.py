# Form imports
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField, DateField, BooleanField, FileField, MultipleFileField, ValidationError
from wtforms.validators import InputRequired, Length
from wtforms.fields.html5 import EmailField
from project.models.tables import User


class LoginForm(FlaskForm):
    email    =  StringField('Email or Username : ')
    password =  PasswordField('Password : ')
    usertype =  StringField('Password : ')
    remember =  BooleanField('Stay signed in')


class SignupForm(FlaskForm):
    username          =  StringField('Email : ', validators=[Length(min=6, max=20, message="Username must be between 6 and 30 characters")])
    email             =  EmailField('Email : ',  validators=[Length(max=80, message="Email must be upto 80 characters")])
    password          =  PasswordField('Password : ')
    confirm_password  =  PasswordField('Confirm password : ')

    def validate_password(self, password):
        SPECIAL_CHARS =['$', '@', '#', '-', '_']
        
        if (len(password.data) > 20) or (len(password.data) < 8):
            print('Password must be upto 40 characters long')
            raise ValidationError('Password must be between 8 to 20 characters')
            
        if not any(char.isdigit() for char in password.data):
            raise ValidationError('Password should have at least one numeral')
            
        if not any(char.isupper() for char in password.data):
            raise ValidationError('Password should have at least one uppercase letter')
            
        if not any(char.islower() for char in password.data):
            raise ValidationError('Password should have at least one lowercase letter')
            
        if not any(char in SPECIAL_CHARS for char in password.data):
            raise ValidationError('Password should have at least one of the symbols $ @ # - _')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()

        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()

        if user:
            raise ValidationError('User with this Email already exists. Please choose a different one.')


class ResetPasswordForm(FlaskForm):
    email_or_username = StringField('Username / Email / Phone number : ')

