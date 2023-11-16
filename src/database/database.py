from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from models import Base  # Import the Base class from models.py

# Define the database URI, this should be configured for your specific environment.
DATABASE_URI = 'sqlite:///legislation_tracker.db'  # or 'postgresql://user:password@localhost/mydatabase'

# Create an engine that stores data in the local directory's legislation_tracker.db file.
engine = create_engine(DATABASE_URI)

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a scoped session
session = scoped_session(SessionLocal)

# Base class for your models from models.py
Base.query = session.query_property()

def init_db():
    # Import all modules here that define models so that
    # they will be registered properly on the metadata.
    # Otherwise you will have to import them before calling init_db()
    import models  # This is the models module you've written previously

    # Create tables for the models
    Base.metadata.create_all(bind=engine)

# Function to close the session
def close_session(exception=None):
    try:
        if exception:
            session.rollback()
        else:
            session.commit()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.remove()

# Example usage within the application context
if __name__ == "__main__":
    # Initialize the database (create tables and relationships)
    init_db()


    
    
