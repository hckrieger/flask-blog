from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, TextAreaField, DateField, RadioField, SelectField, SubmitField
from wtforms.validators import InputRequired, Email, Length, EqualTo
	
class LoginForm(FlaskForm):
	email = StringField('email', validators=[InputRequired(), Email(message='Invalid email'),Length(max=50)])
	password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
	remember = BooleanField('remember me')
	
class RegisterForm(FlaskForm):
	email = StringField('email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
	name = StringField('name', validators=[InputRequired(), Length(min=4, max=15)])
	password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])