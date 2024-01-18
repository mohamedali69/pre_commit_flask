from flask import Flask

from backend.routes.users import users_bp


def create_app():
    app = Flask(__name__)
    app.register_blueprint(users_bp)
    return app
