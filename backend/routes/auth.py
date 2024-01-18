import jwt
from flask import Blueprint, jsonify, request
from werkzeug.security import check_password_hash

auth_bp = Blueprint("auth", __name__)

# Define allowed_users and secret_token here
allowed_users = {
    "username1": "hashed_password1",
    "username2": "hashed_password2",
    # Add more users as needed
}

secret_token = "your_secret_token_here"


@auth_bp.route("/login", methods=["POST"])
def login():
    d = request.json
    if "username" not in d or "password" not in d:
        raise Exception("Unable to authenticate")
    if not check_password_hash(allowed_users[d["username"]], d["password"]):
        raise Exception("Invalid password")

    encoded_jwt = jwt.encode(
        {"sub": 1, "name": "sergio"}, secret_token, algorithm="HS256"
    )
    return jsonify({"token": encoded_jwt})
