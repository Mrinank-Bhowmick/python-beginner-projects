from flask import Flask


def create_app():
    app = Flask(__name__)
    app.secret_key = "AhjcaD8aDAOfa8fnkadsh"  # These are random letters used as the API key for this project.

    from .views import views

    app.register_blueprint(views, url_prefix="/")

    return app
