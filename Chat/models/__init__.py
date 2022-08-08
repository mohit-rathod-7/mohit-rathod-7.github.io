# USE TO CREATE DATABASE
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
import os


template_dir = os.path.relpath('templates/', '__init__.py')
static_dir = os.path.relpath('static/', '__init__.py')

app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

# BASIC CONFIG
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../static/db/database.db'

db = SQLAlchemy(app)


# --------------------------------------------- TABLES --------------------------------------------

class User(UserMixin, db.Model):
    username    =  db.Column(db.String(15),   nullable=False,  primary_key=True)
    firstname   =  db.Column(db.String(20),   nullable=False)
    middlename  =  db.Column(db.String(20),   nullable=False)
    lastname    =  db.Column(db.String(20),   nullable=False)
    profile     =  db.Column(db.String(),     nullable=False)
    password    =  db.Column(db.String(80),   nullable=False)
    type        =  db.Column(db.String(10),   nullable=False)

    def __init__(self, username, firstname, middlename, lastname, profile, password, type):
        self.username   =  username
        self.firstname  =  firstname
        self.middlename =  middlename
        self.lastname   =  lastname
        self.profile    =  profile
        self.password   =  password
        self.type       =  type

    def get_id(self):
        return (self.username)


db.create_all()