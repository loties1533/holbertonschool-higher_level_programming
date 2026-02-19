#!/usr/bin/python3
"""
API flask pour gestion des utilisateurs en mémoire
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}


@app.route("/")
def home():
    """
    retourne un message pour API flask
    """
    return "Welcome to the Flask API!"


@app.route("/data")
def data():
    """
    retourne une liste des noms d utilisateurs en JSON
    """
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    """
    retourne si l API est valide = OK
    """
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    """
    retourne les info completes d un utilisateur donné dans "username"
    si il n existe pas , renvoi une erreur 404
    """
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """
    ajout d un nouvel utilisateur en requete POST
    - verifie que la requête est en JSON
    - Vérifie que le username est bien valide et unique
    - retourne un msg d erreur ou de confirmation si tout est valide
    """
    user_data = request.get_json(silent=True)
    if user_data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    username = user_data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400
    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    users[username] = user_data
    return jsonify({"message": "User added", "user": user_data}), 201


if __name__ == "__main__":
    """
    demarre serveur flask
    """
    app.run(port=5000)
