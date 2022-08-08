# Flask imports
from pydoc import render_doc
from flask import Flask, redirect, render_template, url_for
from flask_jsglue import JSGlue

# Database imports
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Built-In Imports
import os


template_dir = os.path.relpath('templates/', 'app.py')
static_dir = os.path.relpath('static/', 'app.py')


app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)


# BASIC CONFIG
app.config['SECRET_KEY']                   =  'thisissecret'
app.config['SQLALCHEMY_DATABASE_URI']      =  'sqlite:///../static/db/database.db'
app.config['JSONIFY_PRETTYPRINT_REGULAR']  =  False


# LOGIN MANAGER CONFIG
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'


@app.route('/')
def home():
    return redirect(url_for('auth.home'))


@app.errorhandler(404)
def not_found(e):        
    nav_data = {
        "disabled": {
            "home": "",
            "like": "",
            "chat": "",
            "user": "",
        },

        "icon": {
            "home": "outlined",
            "like": "outlined",
            "chat": "outlined",
            "user": "outlined",
        }
    }

    return render_template("error.html", nav_data=nav_data)


db = SQLAlchemy(app)
jsglue = JSGlue(app)