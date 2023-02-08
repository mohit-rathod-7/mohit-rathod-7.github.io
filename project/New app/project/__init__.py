# Built-In Imports
import os

# Flask imports
from datetime import timedelta
from flask import Flask, render_template, redirect, url_for

# Database imports
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


app = Flask(__name__)
db = SQLAlchemy(app, session_options={"autoflush": False})

# BASIC CONFIG
app.config['SECRET_KEY']                =  'thisissecret'
# app.config['SQLALCHEMY_DATABASE_URI']   =  'sqlite:///static/db/database.db'
app.config['SQLALCHEMY_BINDS']          =  {'user': 'sqlite:///static/db/user.db', 'business' : 'sqlite:///static/db/business.db'}
app.config['REMEMBER_COOKIE_DURATION']  =  timedelta(days=7)

# LOGIN MANAGER CONFIG
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view    =  'auth.login'
login_manager.refresh_view  =  'auth.login'


@app.route('/', methods=["GET"])
def home():
    return redirect(url_for("home.dashboard"))


@app.errorhandler(404)
def not_found(e):       
    return render_template("errors/404.html")


@app.errorhandler(500)
def not_found(e):       
    return render_template("errors/500.html")


db.create_all()