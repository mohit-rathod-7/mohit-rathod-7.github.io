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
                    return redirect(url_for('auth.credentials', page_num='1'))

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


@auth.route('/credentials/<page_num>/', methods=['GET', 'POST'])
def credentials(page_num):
    if request.method == "GET":
        if page_num == "1":
            print("ONE")
            return render_template("auth/credentials.html", page_num=page_num, nav_data=nav_data)
        elif page_num == "2":
            print("TWO")
            return render_template("auth/credentials.html", page_num=page_num, nav_data=nav_data)
        elif page_num == "3":
            print("THREE")
            return render_template("auth/credentials.html", page_num=page_num, nav_data=nav_data)
        elif page_num == "4":
            print("FOUR")
            return render_template("auth/credentials.html", page_num=page_num, nav_data=nav_data)
        elif page_num == "5":
            print("FIVE")
            return render_template("auth/credentials.html", page_num=page_num, nav_data=nav_data)
        elif page_num == "6":
            print("SIX")
            return render_template("auth/credentials.html", page_num=page_num, nav_data=nav_data)
        else:
            return ""


    elif request.method == "POST":
        if page_num == "1":
            print("Post : ONE")
            return redirect(url_for('auth.credentials', page_num='2'))
        elif page_num == "2":
            print("Post : TWO")
            return redirect(url_for('auth.credentials', page_num='3'))
        elif page_num == "3":
            print("Post : THREE")
            return redirect(url_for('auth.credentials', page_num='4'))
        elif page_num == "4":
            print("Post : FOUR")
            return redirect(url_for('auth.credentials', page_num='5'))
        elif page_num == "5":
            print("Post : FIVE")
            return redirect(url_for('auth.credentials', page_num='6'))
        elif page_num == "6":
            print("Post : SIX")
            return "End of credentials"


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
