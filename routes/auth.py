from flask import Blueprint, render_template, request,redirect,  url_for
from flask_login import login_user, logout_user, login_required
from models import db
from models.user import User
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint("auth", __name__)

@auth.route("/register", methods=["GET","POST"])
def register():

    if request.method=="POST":
        name=request.form["name"]
        email=request.form["email"]
        password=request.form["password"]

        existing_user=User.query.filter_by(email=email).first()
        if existing_user:
            return "Email already registered!"
        
        hashed_password=generate_password_hash(password)

        new_user=User(
            name=name,
            email=email,
            password=hashed_password
        )
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for("auth.login"))
    
    return render_template("register.html")

@auth.route("/login",methods=["GET","POST"])
def login():
     if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
           login_user(user)
           return redirect(url_for("dashboard"))

        return "Invalid Email or Password"

     return render_template("login.html")

@auth.route("/logout")
@login_required
def logout():

    logout_user()

    return redirect(url_for("auth.login"))