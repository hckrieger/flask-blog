from flask_login import UserMixin
from datetime import datetime
from config import db

class User(UserMixin, db.Model):
	id = db.Column('id', db.Integer, primary_key=True)
	name = db.Column('name', db.String(30), unique=True)
	email = db.Column('email', db.String(50), unique=True)
	password = db.Column('password', db.String(80))
	
	def __init__(self, name, email, password):
		self.name = name
		self.email = email
		self.password = password