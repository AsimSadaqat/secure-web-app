from functools import wraps
from flask import redirect, url_for, flash
from flask_login import current_user

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # 1️⃣ Must be logged in
        if not current_user.is_authenticated:
            return redirect(url_for("main.login"))

        # 2️⃣ Must be admin
        if current_user.role != "admin":
            flash("Access denied: admin only.", "danger")
            return redirect(url_for("main.dashboard"))

        # 3️⃣ Allowed
        return f(*args, **kwargs)

    return decorated_function
