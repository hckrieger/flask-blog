from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, TextAreaField, DateField, RadioField, SelectField, SubmitField
from wtforms.validators import InputRequired, Email, Length, EqualTo
	
class ContactForm(FlaskForm):
	email = StringField('email', validators=[InputRequired(), Email(message='Invalid email'),Length(max=50)])
	body = TextAreaField('body', validators=[InputRequired()])
	send_email = SubmitField()