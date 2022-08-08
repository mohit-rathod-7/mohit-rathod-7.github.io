# Manual imports
import requests, os, random
from views.app import login_manager, db
from models.tables import User
from models.forms import LoginForm, SignupForm

# Flask imports
from flask import Blueprint, render_template, redirect, url_for, request, jsonify, flash, session
from flask_login import login_user, login_required, logout_user, current_user

# Form imports
from wtforms import *
from wtforms.validators import *

# Database imports
from werkzeug.security import generate_password_hash, check_password_hash


auth = Blueprint('auth', __name__)

nav_data = {
    "disabled": {
        "home": "disabled",
        "like": "",
        "chat": "",
        "user": "",
    },

    "icon": {
        "home": "filled",
        "like": "outlined",
        "chat": "outlined",
        "user": "outlined",
    }
}


@auth.route('/')
def home():
    if current_user.is_authenticated == False:
        return render_template("auth/home.html", nav_data=nav_data)
    else:
        return redirect(url_for('recs.home'))


@auth.route('/signup/', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated == False:
        form = SignupForm()

        if form.validate_on_submit() or (request.method == 'POST'):
            try:    
                hashed_password = generate_password_hash(form.password.data, method='sha256')

                new_user =  User(
                                email    = form.email.data.lower(),
                                password = hashed_password,
                            )

                try:
                    db.session.add(new_user)
                    db.session.commit()

                    flash("Successfully Signed up", "success")
                    return redirect(url_for('auth.one'))

                except:
                    flash("This username already exists", "error")
                    print("This username already exists")
                    return render_template("auth/signup.html", form=form, nav_data=nav_data)
            except:
                pass

            # flash here
            
        return render_template("auth/signup.html", form=form, nav_data=nav_data)
    else:
        return redirect(url_for('recs.home'))


@auth.route('/credentials/1/', methods=['GET', 'POST'])
def one():
    return ""


@auth.route('/credentials/2/', methods=['GET', 'POST'])
def two():
    return ""

@auth.route('/credentials/3/', methods=['GET', 'POST'])
def three():
    return ""


@auth.route('/credentials/4/', methods=['GET', 'POST'])
def four():
    return ""


@auth.route('/credentials/5/', methods=['GET', 'POST'])
def five():
    return ""


@auth.route('/credentials/6/', methods=['GET', 'POST'])
def six():
    return ""


@auth.route('/credentials/7/', methods=['GET', 'POST'])
def seven():
    return ""


@auth.route('/credentials/8/', methods=['GET', 'POST'])
def eight():
    return ""


@auth.route('/login/', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated == False:
        form = LoginForm()

        if (request.method == 'POST'):
            next_url = request.form.get("next")
            user = User.query.filter_by(email=form.email.data.lower()).first()

            try:
                if check_password_hash(user.password, form.password.data):
                    login_user(user)

                    db.session.commit()

                    if next_url:
                        flash("Successfully Logged in ", "success")
                        return redirect(next_url)
                    else:
                        flash("Successfully Logged in ", "success")
                        return redirect( url_for('recs.home') )
                else:
                    flash("The username or password is incorrect", "error")
                    return render_template("auth/login.html", form=form, nav_data=nav_data)
            except:
                pass
            flash("Couldn't find username", "error")

        return render_template("auth/login.html", form=form, nav_data=nav_data)
    else:
        return redirect(url_for('recs.home'))
        

@auth.route("/logout/")
@login_required
def logout():
    db.session.commit()
    logout_user()

    flash("Successfully Logged out", "success")
    return redirect(url_for('auth.home'))


@login_manager.user_loader
def load_user(email):
    return User.query.filter_by(email=email).first()
