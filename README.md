# Secure Web Application & Threat Hardening

## 📌 Overview:-

This project is a **secure Flask-based web application** designed to demonstrate
core web security concepts, including:

- Authentication
- Authorization
- Session management
- Role-Based Access Control (RBAC)

The application follows a **defense-in-depth** security approach, ensuring that
multiple layers of protection exist to reduce the impact of vulnerabilities and
prevent unauthorized access or privilege escalation.

---

## 🧱 Project Structure:-

The project follows Flask best practices with a clear separation of concerns
between routing, models, forms, security logic, and templates.

![Project Structure](screenshots/1-project-structure.png)

---

## ▶️ Application Startup:-

The application runs locally using Flask’s development server.

![Flask Running](screenshots/2-flask-running.png)

---

## 🔐 User Registration:-

Users can securely create an account using the registration page.

Security features include:

- Server-side input validation using WTForms
- Email format validation
- CSRF protection using Flask-WTF
- Password hashing using Werkzeug
- Prevention of duplicate account creation

![Register Page](screenshots/3-register-page.png)

---

## 🔑 User Login:-

Registered users can authenticate using their email and password.

Authentication is handled using **Flask-Login**, and passwords are verified using
secure hash comparison.

![Login Page](screenshots/4-login-page.png)

---

## 🧠 Session Management:-

After successful authentication, a secure session is created.

- Protected routes require authentication
- Sessions persist only while the user is logged in
- Logout properly terminates the session

![Dashboard](screenshots/5-dashboard.png)

---

## 🛡️ Role-Based Access Control (RBAC):-

The application enforces **Role-Based Access Control (RBAC)** to restrict access
to sensitive functionality.

Security design includes:

- Each user is assigned a role (`user` or `admin`)
- Admin-only routes are protected using a custom decorator
- Authorization checks are performed after authentication
- Non-admin users are denied access safely

![Admin Page](screenshots/6-admin-page.png)

---

## 🧠 Security Flow (Text-Based Diagram):-

User Request
   ↓
Route Access
   ↓
Authentication Check (Flask-Login)
   ↓
Authorization Check (RBAC Decorator)
   ↓
┌───────────────┬────────────────┐
│ Admin Role    │ User Role      │
│ Access Granted│ Access Denied  │
└───────────────┴────────────────┘

This flow ensures authentication occurs before authorization and prevents
privilege escalation.

---

## 🧪 Input Validation & Protection:-

All user input is validated before processing.

Security measures include:

- WTForms for structured validation
- Email validation
- CSRF protection
- Database constraints for data integrity

---

## 🧯 Threats Mitigated:-

This project mitigates common web application threats such as:

- Unauthorized access
- Privilege escalation
- Credential exposure
- Duplicate or abusive account creation
- Cross-Site Request Forgery (CSRF)

---

## 🛠️ Technologies Used:-

- Python 3
- Flask
- Flask-Login
- Flask-WTF
- SQLAlchemy
- SQLite
- Werkzeug Security Utilities

---

## ✅ Conclusion:-

This project demonstrates a **secure-by-design Flask application** implementing
real-world security patterns used in production systems.

It showcases strong authentication, role-based authorization, session handling,
input validation, and layered security controls.

---

## 📎 Notes:-

- This project is for learning and demonstration purposes
- Flask development server is used for local testing only
- Security features are implemented explicitly for clarity
