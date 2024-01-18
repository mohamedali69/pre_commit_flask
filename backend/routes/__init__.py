import jwt
from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth
from werkzeug.security import check_password_hash, generate_password_hash

allowed_users = {
    "Dali": generate_password_hash("my-password"),
    "Chakhari": generate_password_hash("his-password"),
}

allowed_tokens = {
    "token-dali": "dali",
    "token-chakhari": "chakhari",
}

basic_auth = HTTPBasicAuth()
token_auth = HTTPTokenAuth(scheme="Bearer")

secret_token = "mysecret"


@basic_auth.verify_password
def verify_basic_password(username, password):
    if username not in allowed_users:
        return None

    if check_password_hash(allowed_users[username], password):
        return username


@token_auth.verify_token
def verify_token(token):
    try:
        decoded_jwt = jwt.decode(token, secret_token, algorithms=["HS256"])
    except Exception:
        return None
    if decoded_jwt["name"] in allowed_users:
        return decoded_jwt["name"]
    return None
