from flask import Flask

def create_api_v1(app):
    """Register API version 1 blueprints to the Flask app.

    Args:
        app (Flask): The Flask application instance to which we'll register the blueprints.
    """
    from .api.v1.routes import v1_blueprint
    app.register_blueprint(v1_blueprint, url_prefix='/v1')
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import Config
from .api.routes import api_blueprint
from .blockchain.smart_contracts import SecureSmartContractManager as SmartContractManager
from .blockchain.token_management import SecureTokenManager as TokenManager
from .database.models import db
from .ai_agents.content_creation import ContentCreationAgent  # Manages content creation features using AI
from .ai_agents.productivity_enhancers import ProductivityEnhancer  # Manages productivity enhancement features using AI

def create_app():
    """Create and configure an instance of the Flask application.

    Returns:
        Flask: The created Flask application instance configured with blueprints,
        database, migration tools, and other initialized components.
    """
    """Create and configure an instance of the Flask application.

    Returns:
        Flask: The created Flask application instance configured with blueprints,
        database, migration tools, and other initialized components.
    """
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    Migrate(app, db)

    app.register_blueprint(api_blueprint, url_prefix='/api')  # Register API blueprints with the Flask application

    # Initialize blockchain-related components:
    # The SmartContractManager handles interactions with smart contracts.
    # The TokenManager is responsible for token-related operations.
    app.smart_contract_manager = SmartContractManager(app.config['PRIVATE_KEY'])
    app.token_manager = TokenManager(app.config['PRIVATE_KEY'])

    # Initialize AI-related components:
    # ContentCreationAgent is in charge of AI-driven content creation.
    # ProductivityEnhancer focuses on enhancing user productivity with AI.
    app.content_creation_agent = ContentCreationAgent()
    app.productivity_enhancer = ProductivityEnhancer()

    return app
