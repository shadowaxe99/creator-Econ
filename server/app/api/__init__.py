from flask import Blueprint
from .routes import api_blueprint

def create_api_blueprints(app):
    app.register_blueprint(api_blueprint, url_prefix='/api')