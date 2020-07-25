from flask import flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, ValidationError, TextAreaField
from wtforms.fields.html5 import EmailField
from wtforms.validators import InputRequired, Email, Length, DataRequired, EqualTo
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
    name = StringField('name', validators=[InputRequired(), Length(0, 25)])
    email = EmailField('email', validators=[InputRequired(), Email()])
    subject = StringField('subject', validators=[InputRequired(), Length(0, 50)])
    message = TextAreaField('message', validators=[InputRequired(), Length(10, 500)])
    send = SubmitField('Send')


class FeedbackForm(FlaskForm):
    feedback = TextAreaField('Feedback', validators=[DataRequired()])
    submit = SubmitField('Post')


class RequestResetForm(FlaskForm):
    email = EmailField('email', validators=[InputRequired(), Email()])
    submit = SubmitField('Request Password Reset')

    def validate_email(self, email):
        u = users.query.filter_by(email=email.data).firls

        if u is None:
            raise ValidationError('There is no account that uses this email')


class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired(), Length(9, 25)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), Length(9, 25), EqualTo('password')])
    submit = SubmitField('Reset Password')
