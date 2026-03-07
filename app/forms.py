from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField

# SECURITY TESTING CHANGE
# Originally the application imported strong validators such as:
# DataRequired, Length, Email, EqualTo.
#
# For Week-1 vulnerability testing we intentionally remove most
# validation rules to simulate weak input validation.

from wtforms.validators import DataRequired


class RegisterForm(FlaskForm):

    username = StringField(
        "Username",

        # SECURITY WEAKNESS INTRODUCED
        # Removed Length(min=3, max=150)
        # Now extremely short or malformed usernames can be submitted.
        validators=[DataRequired()]
    )

    email = StringField(
        "Email",

        # SECURITY WEAKNESS INTRODUCED
        # Removed Email() validation and max length restriction.
        # This allows invalid email formats to be submitted.
        validators=[DataRequired()]
    )

    password = PasswordField(
        "Password",

        # SECURITY WEAKNESS INTRODUCED
        # Original secure rule:
        # Length(min=8)
        #
        # Removing this allows extremely weak passwords
        # such as "1" or "abc".
        validators=[DataRequired()]
    )

    confirm_password = PasswordField(
        "Confirm Password",

        # SECURITY WEAKNESS INTRODUCED
        # Original secure rule:
        # EqualTo("password")
        #
        # Removing this allows mismatched passwords.
        validators=[DataRequired()]
    )

    submit = SubmitField("Register")


class LoginForm(FlaskForm):

    email = StringField(
        "Email",

        # SECURITY WEAKNESS INTRODUCED
        # Removed Email() validation so malformed input is accepted.
        validators=[DataRequired()]
    )

    password = PasswordField(
        "Password",

        # Minimal validation only
        validators=[DataRequired()]
    )

    submit = SubmitField("Login")