from flask import Flask, render_template, url_for, request, session, redirect, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from forms import SignUpForm , LoginForm, EmailForm
from Models import users as user

from init import app
from init import db
from init import bcrypt
from init import login_manager
from flask_login import login_user, logout_user, login_required


def list_users():
    return user.query.all()


# instead of rewriting the card html/boostrap layout for each card
# theres  a loop (Jinja2) that iterates over this list and palces the directory in the src
albumImg = ["../static/Pictures/_DSC1002_edited-2.jpg", "../static/Pictures/_DSC0900_edited-2.jpg",
            '../static/Pictures/IMG_20190602_150420955.jpg', "../static/Pictures/IMG_1191.JPG",
            "../static/Pictures/IMG_1190.JPG", "../static/Pictures/DSC_0930.jpg",
            "../static/Pictures/IMG_20190704_211825393.jpg"]
portrait = ["DSC_0930.jpg", "DSC_0685(2).jpg", "DSC_0665.jpg", "DSC_0019.jpg", "DSC_0572.jpg", "DSC_0535.jpg",
            "DSC_0622.jpg", "DSC_0041.jpg", "1.jpg"]

@login_manager.user_loader
def load_user(user_id):
    return user.query.get(int(user_id))


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/register", methods=["POST", "GET"])
def register():
    form = SignUpForm()
    if form.validate_on_submit():
        session.permanent = True
        username = request.form['name']
        email = request.form['email']
        password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user_a = user(username, email, password)
        session['email'] = email
        session['username'] = username
        db.session.add(user_a)
        db.session.commit()
        login_user(user_a)
        return redirect(url_for('index'))
    else:
        return render_template('register.html', form=form, page='register')


@app.route('/login', methods=["POST", "GET"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user_a = user.query.filter_by(name=form.username.data).first()
        if user_a and bcrypt.check_password_hash(user_a.password, form.password.data):
            login_user(user_a)
            session['email'] = user_a.email
            session['username'] = user_a.name
            return redirect(url_for('index'))
        else:
            flash("Wrong username or password please make sure there is no mistake", 'danger')
    return render_template('login.html', form=form, page='login')


@app.route('/logout')
@login_required
def logout():
    session.clear()
    logout_user()
    return redirect(url_for('index'))


@app.route('/about')
def about():
    return render_template("about.html", page="about")


@app.route('/contact', methods=["GET", "POST"])
def contact():
    form = EmailForm()
    email_filler = ""
    name_filler = ""
    if session.get('email'):
        email_filler = session.get('email')
        name_filler = session.get('username')
    if form.validate_on_submit():
        # send email here

        return redirect(url_for('index'))

    return render_template("contact.html", page="contact", form=form, email_filler=email_filler, name_filler=name_filler)


@app.route('/albums')
def albums():
    return render_template('albums.html', albumImg=albumImg, page="album")


@app.route('/users')
@login_required
def users():
    if session.get("username") == "AndreIbrahim":
        return render_template("users.html", page="users", users_list=list_users())
    return redirect(url_for('index'))


@app.route("/albums/album")
def album():
    return render_template('firstAlbum.html', portrait=portrait)


if __name__ == '__main__':
    app.run(debug=True)
