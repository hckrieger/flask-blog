from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://nqrumzgzdzhlcn:195ad27bae6fcc9cf1f9754c9fea7502926a73cb0dcc54edd9fc477bc96539bb@ec2-54-163-227-202.compute-1.amazonaws.com:5432/dbjvasau17m931'

app.config['SECRET_KEY'] = 'thiskeyissupersecret!'



