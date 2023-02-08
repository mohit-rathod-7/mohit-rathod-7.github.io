from project import db

# Database imports
from flask_login import UserMixin


class User(UserMixin, db.Model):
    __bind_key__ = 'user'
    email       =  db.Column(db.String(20),  nullable=False,  unique=True,  primary_key=True)
    password    =  db.Column(db.String(80),  nullable=False)
    key         =  db.Column(db.String(12),  nullable=False,  unique=True)
    created_on  =  db.Column(db.DateTime,    nullable=False)

    def __repr__(self):
        return f"User('{self.email}', '{self.created_on}')"

    def get_id(self):
        return (self.username)


class Business(UserMixin, db.Model):
    __bind_key__ = 'business'
    email       =  db.Column(db.String(20),  nullable=False,  unique=True,  primary_key=True)
    password    =  db.Column(db.String(80),  nullable=False)
    key         =  db.Column(db.String(12),  nullable=False,  unique=True)
    created_on  =  db.Column(db.DateTime,    nullable=False)

    def __repr__(self):
        return f"User('{self.email}', '{self.created_on}')"

    def get_id(self):
        return (self.username)
