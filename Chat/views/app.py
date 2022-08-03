# Flask imports
from flask import Flask
from flask_jsglue import JSGlue

# Database imports
from flask_sqlalchemy import SQLAlchemy

# Built-In Imports
import os


template_dir = os.path.relpath('templates/', 'app.py')
static_dir = os.path.relpath('static/', 'app.py')


app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)


# BASIC CONFIG
app.config['SECRET_KEY'] = 'thisissecret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../static/db/database.db'
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

# RCAPTCHA CONFIG
app.config['RECAPTCHA_USE_SSL'] = False
app.config['RECAPTCHA_PUBLIC_KEY'] ='6LcmFawcAAAAAI175JYBVdXy3pdls_l2degC7hDm'
app.config['RECAPTCHA_PRIVATE_KEY'] ='6LcmFawcAAAAAMqVSb06ZIe5eTLCwHKFP_iOqsbS'
app.config['RECAPTCHA_OPTIONS'] = {'theme': 'dark'}
app.config['TESTING'] = True


# LOGIN MANAGER CONFIG
# login_manager = LoginManager()
# login_manager.init_app(app)
# login_manager.login_view = 'auth.log_in'


# @app.errorhandler(404)
# # inbuilt function which takes error as parameter 
# def not_found(e):
#     return "<h1>error page</h1>"


db = SQLAlchemy(app)
jsglue = JSGlue(app)