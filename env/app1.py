#!/usr/bin/env python

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://localhost/appdb'
SQLALCHEMY_TRACK_MODIFICATIONS = True
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)


db.session.add(User(username="Flask", email="example@example.com"))
db.session.commit()

users = User.query.all()


if __name__ == '__main__':
    
    app.run()