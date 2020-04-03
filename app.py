from flask import Flask, render_template, url_for, request, session, redirect
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy
from forms import *


import forms

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Andre'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFACTIONS"] = False
app.permanent_session_lifetime = timedelta(minutes=5)

db = SQLAlchemy(app)


class users(db.Model):
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


# instead of rewriting the card html/boostrap layout for each card
# theres  a loop (Jinja2) that iterates over this list and palces the directory in the src
albumImg = ["../static/Pictures/_DSC1002_edited-2.jpg", "../static/Pictures/_DSC0900_edited-2.jpg",
            '../static/Pictures/IMG_20190602_150420955.jpg', "../static/Pictures/IMG_1191.JPG",
            "../static/Pictures/IMG_1190.JPG", "../static/Pictures/DSC_0930.jpg",
            "../static/Pictures/IMG_20190704_211825393.jpg"]
portrait = ["DSC_0930.jpg", "DSC_0685(2).jpg", "DSC_0665.jpg", "DSC_0019.jpg", "DSC_0572.jpg", "DSC_0535.jpg",
            "DSC_0622.jpg", "DSC_0041.jpg", "1.jpg"]


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == 'POST':
        session.permanent = True
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        user_a = users(username, email, password)
        session['email'] = email
        session['username'] = username
        db.session.add(user_a)
        db.session.commit()
        return redirect(url_for('index'))
    else:
        form = SignUpForm()
        return render_template('register.html', form=form, page='register')


@app.route('/login')
def login():

    return None


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


@app.route('/about')
def about():
    return render_template("about.html", page="about")


@app.route('/contact')
def contact():
    return render_template("contact.html", page="contact")


@app.route('/albums')
def albums():
    return render_template('albums.html', albumImg=albumImg, page="album")


@app.route("/albums/album")
def album():
    return render_template('firstAlbum.html', portrait=portrait)


if __name__ == '__main__':
    app.run(debug=True)
