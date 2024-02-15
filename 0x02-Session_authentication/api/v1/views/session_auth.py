#!/usr/bin/env python3
"""
handles routes for the Session authentication
"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models.user import User
from os import getenv


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """Session Authentication route"""
    email = request.form.get('email')
    if not email or email == "":
        return jsonify({"error": "email missing"}), 400

    password = request.form.get('password')
    if not password or password == "":
        return jsonify({"error": "password missing"}), 400

    users = User.search({'email': email})
    if not users or users == []:
        return jsonify({"error": "no user found for this email"}), 404

    user: User = users[0]
    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    from api.v1.app import auth
    session_id = auth.create_session(user.id)
    response = jsonify(user.to_json())
    cookie_name = getenv('SESSION_NAME')
    response.set_cookie(cookie_name, session_id)
    return response
