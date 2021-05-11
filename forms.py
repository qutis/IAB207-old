# add missing imports
from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField,SubmitField, StringField, PasswordField
from wtforms.validators import InputRequired, Length, Email, EqualTo

# define the login form
class LoginForm(FlaskForm):
    username = StringField('Username',validators=[InputRequired("Please enter your username")])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('Login')

# define the user registration form
class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    email = StringField('Email', validators=[Email("Please enter an email address")])
    password = PasswordField('Password', validators=[InputRequired(),
        EqualTo('confirm', message="Passwords should match")])
    confirm = PasswordField("Confirm Password")
    submit = SubmitField('Register')