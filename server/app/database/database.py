from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from .models import Base
import os

# Configure the SQLAlchemy part of the app instance
database_uri = os.getenv('DATABASE_URL', 'sqlite:///elysium_marketplace.db')
engine = create_engine(database_uri, convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

# Initialize the database helper object
db = SQLAlchemy()

def init_db():
    # Import all modules here that might define models so that
    # they will be registered properly on the metadata. Otherwise
    # you will have to import them first before calling init_db()
    import server.app.database.models

    Base.metadata.create_all(bind=engine)

def shutdown_session(exception=None):
    db_session.remove()