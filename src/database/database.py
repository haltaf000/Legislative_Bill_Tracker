from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base, Bill
from src.config import Config

engine = create_engine(Config.DATABASE_URI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def get_db_session():
    db_session = SessionLocal()
    try:
        yield db_session
    finally:
        db_session.close()

    
    
