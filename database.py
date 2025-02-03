# database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database URL
DATABASE_URL = "sqlite:///database.db"

# Create the engine
engine = create_engine(DATABASE_URL)

# Create a configured Session class
Session = sessionmaker(bind=engine)

# Create a Session instance
session = Session()

# Base for models
Base = declarative_base()