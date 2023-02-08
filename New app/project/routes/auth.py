from project import db, login_manager
from project.models.tables import User, Business
from project.models.forms import LoginForm, SignupForm, ResetPasswordForm

# Flask imports
from flask import Blueprint, render_template, redirect, url_for, request, jsonify, flash, session
from flask_login import login_user, login_required, logout_user, current_user, fresh_login_required

# Form imports
from wtforms import *
from wtforms.validators import *

# Database imports
from werkzeug.security import generate_password_hash, check_password_hash


auth = Blueprint('auth', __name__)


@auth.route('/')
def home():
    if current_user.is_authenticated == False:
        return redirect(url_for('auth.login'))
    else:
        return redirect(url_for('home.dashboard'))


@auth.route('/signup/', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated == False:
        return render_template("auth/auth.html")
    else:
        return redirect(url_for('home.dashboard'))


@auth.route('/login/', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated == False:
        form = LoginForm()

        return render_template("auth/login.html", form=form)
    else:
        return redirect(url_for('home.dashboard'))


@auth.route('/login/business/', methods=['GET', 'POST'])
def login_business():
    if current_user.is_authenticated == False:
        form = LoginForm()

        if form.validate_on_submit():
            next_url = request.form.get("next")
            user = Business.query.filter((Business.email == form.email.data.lower())).first()

            if user and check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                flash("Successfully Logged in ", "success")
    
                return redirect(next_url) if next_url else redirect(url_for('home.dashboard'))
            else:
                flash("Login unsuccessful. Please check email or password", "error")
                return render_template("auth/login.html", form=form)

        return render_template("auth/login.html", form=form)
    else:
        return redirect(url_for('home.dashboard'))



@auth.route('/login/user/', methods=['GET', 'POST'])
def login_user():
    if current_user.is_authenticated == False:
        form = LoginForm()

        if form.validate_on_submit():
            next_url = request.form.get("next")
            user = User.query.filter((User.email == form.email.data.lower())).first()

            if user and check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                flash("Successfully Logged in ", "success")
    
                return redirect(next_url) if next_url else redirect(url_for('home.dashboard'))
            else:
                flash("Login unsuccessful. Please check email or password", "error")
                return render_template("auth/login.html", form=form)

        return render_template("auth/login.html", form=form)
    else:
        return redirect(url_for('home.dashboard'))


@auth.route("/reset_password/", methods=['GET', 'POST'])
def reset_password():
    form = ResetPasswordForm()

    if request.method == "POST":
        user = User.query.filter((User.email == form.email_or_username.data.lower()) | (User.username == form.email_or_username.data.lower())).first()
 
        # with mail.connect() as conn:
        #     msg = Message("Reset password link", recipients=[user.email])
        #     msg.html = "<b>To reset password : </b><a href='#'>Click here</a>"
        #     conn.send(msg)
        # ERROR : smtplib.SMTPAuthenticationError: (535, b'5.7.8 Username and Password not accepted.
        
        return redirect(url_for('auth.home'))

    return render_template("auth/reset_password.html", form=form)
        

@auth.route("/logout/")
@login_required
def logout():
    db.session.commit()
    logout_user()

    flash("Successfully Logged out", "success")
    return redirect(url_for('auth.home'))


@login_manager.user_loader
def load_user(username):
    return User.query.filter_by(username=username).first()

