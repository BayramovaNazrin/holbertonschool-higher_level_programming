#!/usr/bin/python3
"""
API Security with Basic Auth and JWT Authentication.
"""

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity, get_jwt
)
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
auth = HTTPBasicAuth()

# Secret key for JWT
app.config["JWT_SECRET_KEY"] = "super-secret-key"
jwt = JWTManager(app)

# In-memory users
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}

# ---------------------------
# BASIC AUTHENTICATION
# ---------------------------

@auth.verify_password
def verify_password(username, password):
    user = users.get(username)
    if not user:
        return None
    if check_password_hash(user["password"], password):
        return username
    return None


@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"


# ---------------------------
# JWT LOGIN
# ---------------------------

@app.route("/login", methods=["POST"])
def login():
    try:
        data = request.get_json(force=True)
    except Exception:
        return jsonify({"error": "Invalid JSON"}), 401

    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "Invalid credentials"}), 401

    user = users.get(username)
    if not user:
        return jsonify({"error": "Invalid credentials"}), 401

    if not check_password_hash(user["password"], password):
        return jsonify({"error": "Invalid credentials"}), 401

    # Create token with role inside
    token = create_access_token(identity=username, additional_claims={"role": user["role"]})

    return jsonify({"access_token": token}), 200


# ---------------------------
# JWT PROTECTED ROUTES
# ---------------------------

@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted"


@app.route("/admin-only")
@jwt_required()
def admin_only():
    claims = get_jwt()
    role = claims.get("role")

    if role != "admin":
        return jsonify({"error": "Admin access required"}), 403

    return "Admin Access: Granted"


# ---------------------------
# JWT ERROR HANDLERS (ALL MUST RETURN 401)
# ---------------------------

@jwt.unauthorized_loader
def missing_token(err):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def invalid_token(err):
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def expired_token(jwt_header, jwt_payload):
    return jsonify({"error": "Token has expired"}), 401

@jwt.revoked_token_loader
def revoked_token(jwt_header, jwt_payload):
    return jsonify({"error": "Token has been revoked"}), 401

@jwt.needs_fresh_token_loader
def needs_fresh_token(err):
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == "__main__":
    app.run()
