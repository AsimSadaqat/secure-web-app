class Config:

    # -----------------------------
    # ORIGINAL SECURE SETTING
    # -----------------------------
    # This prevents SQLAlchemy from tracking every object modification,
    # which improves performance and avoids unnecessary memory usage.
    SQLALCHEMY_TRACK_MODIFICATIONS = False


    # -----------------------------
    # SECURITY WEAKNESS INTRODUCED
    # -----------------------------
    # Originally this was set to True, which prevents JavaScript
    # from accessing session cookies.
    #
    # Setting this to False allows client-side scripts to read
    # the session cookie.
    #
    # Risk: If an attacker successfully injects JavaScript (XSS),
    # they could steal the session cookie and hijack the user session.
    SESSION_COOKIE_HTTPONLY = False


    # -----------------------------
    # SECURITY WEAKNESS INTRODUCED
    # -----------------------------
    # Originally: "Lax"
    #
    # "Lax" provides some protection against Cross-Site Request Forgery.
    #
    # Setting it to None removes this protection and allows cookies
    # to be sent with cross-site requests.
    #
    # Risk: Attackers could exploit CSRF attacks more easily.
    SESSION_COOKIE_SAMESITE = None


    # -----------------------------
    # SECURITY WEAKNESS INTRODUCED
    # -----------------------------
    # CSRF protection intentionally disabled for security testing.
    #
    # This simulates a Cross-Site Request Forgery vulnerability.
    #
    # Risk: Attackers could trick logged-in users into submitting
    # malicious requests from another website.
    WTF_CSRF_ENABLED = False