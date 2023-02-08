from project import db
from flask import Blueprint, redirect, url_for, render_template


home = Blueprint('home', __name__)


@home.route('/dashboard/', methods=["GET"])
def dashboard():
    return render_template('home/home.html')

