from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required
# NOTE: admin_required decorator intentionally NOT imported here
# This is done to simulate a Broken Access Control vulnerability for security testing.

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

        # -----------------------------
        # SECURITY WEAKNESS INTRODUCED
        # -----------------------------
        # Original secure code used:
        # user.set_password(form.password.data)
        #
        # That function hashes the password before storing it.
        #
        # For Week-1 security testing, we intentionally store the password
        # directly in plaintext to simulate a "Weak Password Storage"
        # vulnerability.
        #
        # Risk: If the database is compromised, attackers can immediately
        # read all user passwords.
        user.password = form.password.data

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

        # -----------------------------
        # SECURITY WEAKNESS INTRODUCED
        # -----------------------------
        # Original secure code used:
        # user.check_password(form.password.data)
        #
        # That function compares the password hash safely.
        #
        # For the insecure testing version, we directly compare plaintext
        # passwords. This simulates weak authentication logic and allows
        # easier password compromise.
        #
        # Risk: Attackers could potentially exploit weak password storage
        # and bypass secure authentication mechanisms.
        if user and user.password == form.password.data:
            login_user(user)
            return redirect(url_for("main.dashboard"))

        flash("Invalid email or password", "danger")

    return render_template("login.html", form=form)


@main.route("/dashboard")
@login_required
def dashboard():

    # -----------------------------
    # SECURITY WEAKNESS INTRODUCED
    # -----------------------------
    # Here we intentionally expose the user's IP address.
    # While not always critical, unnecessary exposure of
    # internal or identifying data is considered
    # "Information Disclosure".
    #
    # Risk: Attackers can gather information about the user
    # environment or infrastructure.
    return f"You are logged in. Session is active. Your IP: {request.remote_addr}"


@main.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.login"))


@main.route("/admin")
@login_required

# -----------------------------
# SECURITY WEAKNESS INTRODUCED
# -----------------------------
# Original secure code used:
# @admin_required
#
# That decorator ensured only administrators could access
# this route.
#
# It has been intentionally removed to simulate a
# "Broken Access Control / Privilege Escalation" vulnerability.
#
# Risk: Any authenticated user can now access admin-only
# functionality.
def admin_panel():
    return "Welcome Admin. You have elevated privileges."