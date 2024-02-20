#!/usr/bin/env python3
"""
Flask app Module
"""
from auth import Auth
from flask import Flask, jsonify, request, abort

app = Flask(__name__)
AUTH = Auth()


@app.route("/")
def home():
    """home route"""
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"])
def users():
    """register new user route"""
    email = request.form.get("email")
    password = request.form.get("password")

    try:
        AUTH.register_user(email, password)
        return jsonify({"email": f"{email}", "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route("/sessions", methods=["POST"])
def sessions():
    """sessions route handler"""
    email = request.form.get("email")
    password = request.form.get("password")
    if AUTH.valid_login(email, password):
        AUTH.create_session(email)
        return jsonify({"email": f"{email}", "message": "logged in"})
    abort(401)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
