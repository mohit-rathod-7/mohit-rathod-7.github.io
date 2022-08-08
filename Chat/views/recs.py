# Flask imports
from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user, login_required


recs = Blueprint('recs', __name__)

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


@recs.route('/')
@login_required
def home():
    return render_template("home/recs.html", nav_data=nav_data)
        

@recs.route('/like/', methods=['GET'])
@login_required
def like():
    return render_template("home/card.html")

    
@recs.route('/dislike/', methods=['GET'])
@login_required
def dislike():
    return render_template("home/card.html")