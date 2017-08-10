from datetime import datetime
from config import db

class Post(db.Model):
	id = db.Column('id', db.Integer, primary_key=True)
	title = db.Column('title', db.String(90), unique=True)
	slug = db.Column('slug', db.String(90))
	body = db.Column('body', db.Text())
	created_at = db.Column('created_at', db.DateTime(timezone=True), default=datetime.now(), nullable=True)
	category = db.Column('category', db.String(60), nullable=True)
	author = db.Column('author', db.String(90))
	user_id = db.Column('user_id', db.Integer, db.ForeignKey('user.id'))
	
	def __init__(self, title, slug, body, category, author, user_id):
		self.title = title
		self.slug = slug
		self.body = body
		self.category = category
		self.author = author,
		self.user_id = user_id
		
class Draft(db.Model):
	id = db.Column('id', db.Integer, primary_key=True)
	title = db.Column('title', db.String(90), unique=True)
	slug = db.Column('slug', db.String(90))
	created_at = db.Column('created_at', db.DateTime(timezone=True), default=datetime.now(), nullable=True)
	body = db.Column('body', db.Text())
	category = db.Column('category', db.String(60))
	author = db.Column('author', db.String(90))
	user_id = db.Column('user_id', db.Integer, db.ForeignKey('user.id'))

	
	def __init__(self, title, slug, body, author, category, user_id):
		self.title = title
		self.slug = slug
		self.body = body
		self.author = author
		self.category = category
		self.user_id = user_id