from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required
from .decorators import admin_required
from .forms import RegisterForm, LoginForm
from .models import User, SecurityLog  # Added SecurityLog model for logging events
from .extensions import db

main = Blueprint("main", __name__)


# -------------------------------
# Homepage
# -------------------------------
@main.route("/")
def home():
    return render_template("home.html")


# -------------------------------
# Register
# -------------------------------
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


# -------------------------------
# Login
# -------------------------------
@main.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():

        user = User.query.filter_by(email=form.email.data).first()

        if user and user.check_password(form.password.data):
            login_user(user)
            flash("Login successful!", "success")
            return redirect(url_for("main.dashboard"))

        # -------------------------------
        # SECURITY FEATURE
        # Log failed login attempts
        # -------------------------------
        log = SecurityLog(
            event_type="failed_login",
            email=form.email.data,
            ip_address=request.remote_addr
        )

        db.session.add(log)
        db.session.commit()

        # -------------------------------
        # BRUTE FORCE DETECTION
        # If same email fails 5+ times
        # -------------------------------
        recent_attempts = SecurityLog.query.filter_by(
            email=form.email.data,
            event_type="failed_login"
        ).count()

        if recent_attempts >= 5:
            brute_log = SecurityLog(
                event_type="brute_force_attempt",
                email=form.email.data,
                ip_address=request.remote_addr
            )
            db.session.add(brute_log)
            db.session.commit()

        flash("Invalid email or password.", "danger")

    return render_template("login.html", form=form)


# -------------------------------
# Dashboard
# -------------------------------
@main.route("/dashboard")
@login_required
def dashboard():
    return "You are logged in. Session is active."


# -------------------------------
# Logout
# -------------------------------
@main.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You have been logged out.", "info")
    return redirect(url_for("main.login"))


# -------------------------------
# Admin Panel
# -------------------------------
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



