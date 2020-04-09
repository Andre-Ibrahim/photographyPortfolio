
from init import db
from flask_login import UserMixin


class users(db.Model, UserMixin):
    _id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    password = db.Column(db.String(100))

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def __repr__(self):
        return f"users('{self.name}', '{self.email}' ,'{self.password}')"

    def get_name(self):
        return self.name

    def get_id(self):
        return self._id

    def get_email(self):
        return self.email
