
from init import db, app
from flask_login import UserMixin
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

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

    def get_reset_token(self, expires_sec=1800):
        s = Serializer(app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self._id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return users.query.get(user_id)

    def get_name(self):
        return self.name

    def get_id(self):
        return self._id

    def get_email(self):
        return self.email


class Feedback(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    content = db.Column(db.Text, nullable=False)
    date = db.Column(db.String(100))

    def __init__(self, username, content, date):
        self.username = username
        self.content = content
        self.date = date

    def __repr__(self):
        return f"Feedback('{self.username}', '{self.content}', '{self.date}')"
