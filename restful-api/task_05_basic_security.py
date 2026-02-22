#!/usr/bin/python3
"""
API Flask avec authentification Basic, JWT et contrôle d'accès par role
"""

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required,
    get_jwt
)

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "super-secret-key"

auth = HTTPBasicAuth()
jwt = JWTManager(app)

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


def verify_password(username, password):
    """
    vérifie les identifiants pour l'authentification Basic
    """
    user = users.get(username)
    if not user:
        return None
    if not check_password_hash(user["password"], password):
        return None
    return username


auth.verify_password(verify_password)


@app.route("/basic-protected", methods=["GET"])
@auth.login_required
def basic_protected():
    """
    route protégée par authentification Basic
    """
    return "Basic Auth: Access Granted", 200


@app.route("/login", methods=["POST"])
def login():
    """Connexion utilisateur et génération d'un token JWT."""
    data = request.get_json(silent=True)

    if not data:
        return jsonify({"error": "Invalid JSON"}), 401

    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "Username and password required"}), 401

    user = users.get(username)
    if not user or not check_password_hash(user["password"], password):
        return jsonify({"error": "Invalid credentials"}), 401

    additional_claims = {"role": user["role"]}
    access_token = create_access_token(
        identity=username,
        additional_claims=additional_claims
    )

    return jsonify({"access_token": access_token}), 200


@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def jwt_protected():
    """
    route protégée par authentification JWT
    """
    return "JWT Auth: Access Granted", 200


@app.route("/admin-only", methods=["GET"])
@jwt_required()
def admin_only():
    """
    route accessible uniquement aux administrateur
    """
    claims = get_jwt()
    role = claims.get("role")

    if role != "admin":
        return jsonify({"error": "Admin access required"}), 403

    return "Admin Access: Granted", 200


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """
    gere l'absence ou l'invalidité du token JWT
    """
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """
    gère les tokens JWT invalides
    """
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(jwt_header, jwt_payload):
    """Gère les tokens JWT expiré"""
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(jwt_header, jwt_payload):
    """
    gere les tokens pour une authentification fraîche
    """
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == "__main__":
    """
    lance l'app Flask
    """
    app.run()
