# Manual Imports
from datetime import datetime
from views.app import db
from models.relationships import *


# Database imports
from flask_login import UserMixin


# --------------------------------------------- TABLES --------------------------------------------

class User(UserMixin, db.Model):
    email    =  db.Column(db.String(15),   nullable=False,  primary_key=True)
    password =  db.Column(db.String(80),   nullable=False)


    def __init__(self, email, password):
        self.email    =  email
        self.password =  password

    def get_id(self):
        return (self.email)
