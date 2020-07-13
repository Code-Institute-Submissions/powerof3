from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,TextAreaField
from wtforms.validators import DataRequired,Email,EqualTo,Length
from wtforms import ValidationError
from flask_wtf.file import FileField,FileAllowed

from flask_login import current_user
from po3.models import User

class LoginForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired()],)
    submit = SubmitField('Log In')

class RegistrationForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])
    username = StringField('Username',validators=[DataRequired()])
    first_name = StringField('First name',validators=[DataRequired()])  
    last_name = StringField('Last name',validators=[DataRequired()])
    password = PasswordField('Password',validators=[DataRequired(),EqualTo('password_confirm')])
    password_confirm = PasswordField('Confirm Password',validators=[DataRequired()])
    submit = SubmitField('Register')

    def check_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('This email is already registered, please enter another email.')

    def check_username(self,field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('This username is already taken, please enter another username.')

class UpdateUserForm(FlaskForm):

    email = StringField('Email',validators=[DataRequired(),Email()])
    username = StringField('Username',validators=[DataRequired()])
    profile_image = FileField('Update profile picture',validators=[FileAllowed(['jpg','png','jpeg'])])
    short_story = TextAreaField('My Short story',validators=[DataRequired(),Length(max=200)])
    submit = SubmitField('Update')

    def check_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('This email is already registered, please enter another email.')

    def check_username(self,field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('This username is already taken, please enter another username.')




