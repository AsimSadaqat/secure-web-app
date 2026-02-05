from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from .decorators import admin_required
from .forms import RegisterForm, LoginForm
from .models import User
from .extensions import db
from sqlalchemy.exc import IntegrityError

main = Blueprint("main", __name__)


@main.route("/")
def home():
    return "Secure Web App is running"


@main.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        existing_user = User.query.filter_by(email=form.email.data).first()
        if existing_user:
            flash("Email already registered. Please log in.", "warning")
            return redirect(url_for("main.login"))

        user = User(
            username=form.username.data,
            email=form.email.data
        )
        user.set_password(form.password.data)

        try:
            db.session.add(user)
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            flash("Registration failed. Try a different email.", "danger")
            return redirect(url_for("main.register"))

        flash("Account created successfully. Please log in.", "success")
        return redirect(url_for("main.login"))

    return render_template("register.html", form=form)


@main.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect(url_for("main.dashboard"))

        flash("Invalid email or password", "danger")

    return render_template("login.html", form=form)


@main.route("/dashboard")
@login_required
def dashboard():
    return "You are logged in. Session is active."


@main.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.login"))


@main.route("/admin")
@login_required
@admin_required
def admin_panel():
    return "Welcome Admin. You have elevated privileges."
