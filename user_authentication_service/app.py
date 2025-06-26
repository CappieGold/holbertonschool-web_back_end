#!/usr/bin/env python3
"""
Flask app
"""
from flask import Flask, jsonify, request
from auth import Auth
import flask


AUTH = Auth()

app = Flask(__name__)


@app.route("/", methods=['GET'])
def bienvenue():
    """
    GET / route that returns a welcome message
    """
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=['POST'])
def users():
    """
    POST /users route to register a new user
    """
    email = request.form.get('email')
    password = request.form.get('password')

    try:
        user = AUTH.register_user(email, password)
        return jsonify({
            "email": email,
            "message": "user created"
        })
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route("/sessions", methods=['POST'])
def login():
    """
    POST /sessions route to log in a user
    """
    email = request.form.get('email')
    password = request.form.get('password')

    if AUTH.valid_login(email, password):
        session_id = AUTH.create_session(email)
        response = jsonify({
            "email": email,
            "message": "logged in",
        })
        response.set_cookie("session_id", session_id)
        return response
    else:
        return flask.abort(401)


@app.route("/sessions", methods=['DELETE'])
def logout():
    """
    DELETE /sessions route to log out a user
    """
    session_id = request.cookies.get("session_id")

    user = AUTH.get_user_from_session_id(session_id)
    if not user:
        return flask.abort(403)

    AUTH.destroy_session(user.id)
    return flask.redirect("/", 302)


@app.route("/profile", methods=['GET'])
def profile():
    """
    GET /profile route to get user profile
    """
    session_id = request.cookies.get("session_id")

    user = AUTH.get_user_from_session_id(session_id)

    try:
        response = jsonify({
            "email": user.email
        })
        response.status_code = 200
        return response
    except AttributeError:
        return flask.abort(403)


@app.route("/reset_password", methods=['POST'])
def get_reset_password_token():
    """
    POST /reset_password route to get reset password token
    """
    email = request.form.get('email')

    try:
        reset_token = AUTH.get_reset_password_token(email)
        return jsonify({
            "email": email,
            "reset_token": reset_token
        }), 200
    except ValueError:
        flask.abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
