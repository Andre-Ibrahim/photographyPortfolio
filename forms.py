from flask import flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, ValidationError, TextAreaField
from wtforms.fields.html5 import EmailField
from wtforms.validators import InputRequired, Email, Length
from Models import users


class SignUpForm(FlaskForm):
    name = StringField('username', validators=[InputRequired(), Length(min=9, max=25)])
    email = EmailField('email', validators=[InputRequired(), Email()])
    password = PasswordField('password', validators=[InputRequired(), Length(min=9, max=25)])
    submit = SubmitField('Sign up')

    def validate_name(self, name):
        u = users.query.filter_by(name=name.data).first()
        if u:
            raise ValidationError('That username is already taken')

    def validate_email(self, email):
        u = users.query.filter_by(email=email.data).first()
        if u:
            raise ValidationError('That email is already taken')


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(9, 25)])
    password = PasswordField('Password', validators=[InputRequired(), Length(9, 25)])
    submit = SubmitField('Login')


class EmailForm(FlaskForm):
    name = StringField('Username', validators=[InputRequired(), Length(9, 25)])
    email = EmailField('email', validators=[InputRequired(), Email()])
    subject = StringField('Username', validators=[InputRequired(), Length(0, 50)])
    message = TextAreaField('message', validators=[InputRequired(), Length(20, 500)])
    send = SubmitField('Send')




