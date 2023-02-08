from project import db, login_manager
from project.models.tables import User, Business
from project.models.forms import LoginForm, SignupForm, ResetPasswordForm

# Flask imports
from flask import Blueprint, render_template, redirect, url_for, request, jsonify, flash, session
from flask_login import login_user, login_required, logout_user, current_user, fresh_login_required

# Form imports
from wtforms import *
from wtforms.validators import *


calendar = Blueprint('calendar', __name__)


@calendar.route('/')
@login_required
def home():
    return render_template('calendar/calendar.html')

