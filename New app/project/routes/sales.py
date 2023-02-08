from project import db, login_manager
from project.models.tables import User, Business
from project.models.forms import LoginForm, SignupForm, ResetPasswordForm

# Flask imports
from flask import Blueprint, render_template, redirect, url_for, request, jsonify, flash, session
from flask_login import login_user, login_required, logout_user, current_user, fresh_login_required

# Form imports
from wtforms import *
from wtforms.validators import *


sales = Blueprint('sales', __name__)


@sales.route('/')
@login_required
def home():
    return redirect(url_for('sales.daily_sales'))


@sales.route('/daily_sales/')
@login_required
def daily_sales():
    return render_template('sales/sales.html')


@sales.route('/appointments/')
@login_required
def appointments():
    return render_template('sales/appointments.html')


@sales.route('/invoices/')
@login_required
def invoices():
    return render_template('sales/invoices.html')


@sales.route('/vouchers/')
@login_required
def vouchers():
    return render_template('sales/vouchers.html')


@sales.route('/paid_plans')
@login_required
def paid_plans():
    return render_template('sales/paid_plans.html')

