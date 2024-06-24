from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, DateField, PasswordField, SubmitField, BooleanField
 
from wtforms.validators import DataRequired, Length, Email

class Signup_Form(FlaskForm):
    username = StringField('username', validators=[DataRequired(), Length(4, 6)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[Length(4, 11)])
    signup = SubmitField('Sign Up')
    
class Login_Form(FlaskForm):
    username = StringField('username', validators=[DataRequired(), Length(4, 6)])
    password = PasswordField('Password', validators=[Length(4, 11)])
    login = SubmitField('Login')

class Details_Form(FlaskForm):
    pass