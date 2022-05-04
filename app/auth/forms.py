from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import InputRequired, Email,EqualTo
from .. models import User



class RegistrationForm(FlaskForm):
    email = StringField('Your email address',validators=[InputRequired(),Email()])
    username = StringField('Your username',validators=[InputRequired()])
    password = PasswordField('Your password',validators=[InputRequired(),
            EqualTo('password_confirm', message = 'Passwords must match')])
    password_confirm = PasswordField('Confirm Password',validators=[InputRequired()])
    submit = SubmitField('Sign Up')
    