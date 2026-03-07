from datetime import datetime
from flask_login import UserMixin
from .extensions import db

# SECURITY TESTING CHANGE:
# The original secure version imported password hashing utilities:
# from werkzeug.security import generate_password_hash, check_password_hash
#
# For Week-1 vulnerability testing, hashing is intentionally removed
# to simulate insecure password storage.


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)

    # SECURITY WEAKNESS INTRODUCED
    # Passwords will now be stored in plaintext instead of hashed.
    password_hash = db.Column(db.String(256), nullable=False)

    role = db.Column(db.String(50), default="user", nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def set_password(self, password):

        # --------------------------------------------------
        # SECURITY TESTING CHANGE
        # --------------------------------------------------
        # Original secure code:
        #
        # self.password_hash = generate_password_hash(password)
        #
        # That hashes the password before storing it.
        #
        # For Week-1 testing we intentionally store the password
        # directly without hashing.
        #
        # This simulates the vulnerability:
        # "Plaintext Password Storage".
        #
        # Risk in real systems:
        # If the database is leaked, attackers can immediately
        # read all user passwords.
        # --------------------------------------------------

        self.password_hash = password

    def check_password(self, password):

        # --------------------------------------------------
        # SECURITY TESTING CHANGE
        # --------------------------------------------------
        # Original secure code:
        #
        # return check_password_hash(self.password_hash, password)
        #
        # Instead we compare plaintext values directly.
        #
        # This demonstrates insecure authentication logic.
        # --------------------------------------------------

        return self.password_hash == password

    def __repr__(self):
        return f"<User {self.username}>"

