from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import Config
from .api.routes import api_blueprint
from .blockchain.smart_contracts import SmartContractManager
from .blockchain.token_management import TokenManager
from .database.models import db
from .ai_agents.content_creation import ContentCreationAgent
from .ai_agents.productivity_enhancers import ProductivityEnhancer

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    Migrate(app, db)

    app.register_blueprint(api_blueprint, url_prefix='/api')

    # Initialize blockchain managers
    app.smart_contract_manager = SmartContractManager()
    app.token_manager = TokenManager()

    # Initialize AI agents
    app.content_creation_agent = ContentCreationAgent()
    app.productivity_enhancer = ProductivityEnhancer()

    return app
