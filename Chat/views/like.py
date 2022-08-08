# Flask imports
from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user, login_required


like = Blueprint('like', __name__)

nav_data = {
    "disabled": {
        "home": "",
        "like": "disabled",
        "chat": "",
        "user": "",
    },

    "icon": {
        "home": "outlined",
        "like": "filled",
        "chat": "outlined",
        "user": "outlined",
    }
}


@like.route('/')
@login_required
def home():
    return render_template("like/like.html", nav_data=nav_data)
        