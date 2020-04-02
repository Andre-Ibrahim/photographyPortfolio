from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.fields.html5 import EmailField
from wtforms.validators import InputRequired, Email


class SignUpForm(FlaskForm):
    username = StringField('username', validators=[InputRequired()])
    email = EmailField('email', validators=[InputRequired(), Email()])
    password = PasswordField('password', validators=[InputRequired()])
    submit = SubmitField('Sign up')


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('Login')

