# Flask imports
from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user, login_required


user = Blueprint('user', __name__)

nav_data = {
    "disabled": {
        "home": "",
        "like": "",
        "chat": "",
        "user": "disabled",
    },

    "icon": {
        "home": "outlined",
        "like": "outlined",
        "chat": "outlined",
        "user": "filledoutlined",
    }
}


@user.route('/')
@login_required
def home():
    return render_template("user/user.html", nav_data=nav_data)
        