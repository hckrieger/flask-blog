from config import app
from flask import Flask
from models import authentication, posts
from views import authentication, posts
from forms import authentication, posts

if __name__ == '__main__':
	app.run(port=33507)
	