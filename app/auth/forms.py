# from django.forms import ValidationError
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField, ValidationError,BooleanField
from wtforms.validators import InputRequired, Email,EqualTo
from .. models import User



class RegistrationForm(FlaskForm):
    email = StringField('Your email address',validators=[InputRequired(),Email()])
    def validate_email(self,data_field):
        if User.query.filter_by(email=data_field.data).first():
            raise ValidationError('There is already a registration with that email address')
    
    username = StringField('Your username',validators=[InputRequired()])
    def validate_username(self,data_field):
        if User.query.filter(username=data_field.data).first():
            raise ValidationError('There is already a registration with that username')
    
    password = PasswordField('Your password',validators=[InputRequired(),
            EqualTo('password_confirm', message = 'Passwords must match')])

    password_confirm = PasswordField('Confirm Password',validators=[InputRequired()])
    
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
        email = StringField('Your Email Address',validators=[InputRequired(),Email()])
        password = PasswordField('Password',validators =[InputRequired()])
        remember = BooleanField('Remember me')
        submit = SubmitField('Sign In')