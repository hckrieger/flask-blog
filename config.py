from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://eanmrvhallmyjz:90029caff260aad01581dfaf11bd2d5e654a8940322543564110b61021895789@ec2-23-21-85-76.compute-1.amazonaws.com:5432/d6328ucq1kvuvj'

app.config['SECRET_KEY'] = 'thiskeyissupersecret!'



