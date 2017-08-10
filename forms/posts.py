from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, TextAreaField, DateField, RadioField, SelectField, SubmitField
from wtforms.validators import InputRequired, Email, Length, EqualTo

class PostForm(FlaskForm):
	title = StringField('title', validators=[InputRequired()])
	slug = StringField('slug', validators=[InputRequired()])
	category = SelectField('category', choices=[('general', 'general'), ('economics', 'economics'), ('music', 'music'), ('government', 'government'), ('video games', 'video games'), ('psychology', 'psychology'), ('technology', 'technology')],  validators=[InputRequired()])
	body = TextAreaField('body', validators=[InputRequired()])
	create_draft = SubmitField()
	create_post = SubmitField()
	update_draft = SubmitField()
	update_post = SubmitField()