from functools import wraps
from flask import redirect, url_for, flash
from flask_login import current_user

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):

        # --------------------------------------------------
        # SECURITY TESTING CHANGE
        # --------------------------------------------------
        # Original secure logic checked:
        #
        # 1) if user is authenticated
        # 2) if user role == "admin"
        #
        # If the user was not an admin, access to admin routes
        # such as /admin would be blocked.
        #
        # For Week-1 vulnerability testing, the authorization
        # checks are intentionally bypassed so ANY authenticated
        # user can access admin functionality.
        #
        # This simulates a classic OWASP vulnerability:
        # Broken Access Control / Privilege Escalation.
        #
        # Risk in real systems:
        # A normal user could gain admin privileges and access
        # sensitive functionality or data.
        #
        # NOTE:
        # This change exists only in the `week1-insecure-version`
        # branch for controlled security testing.
        # --------------------------------------------------

        return f(*args, **kwargs)

    return decorated_function