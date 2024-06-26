from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
from os import getenv
import pymysql


# Get the database connection string from the environment variables
database_uri = getenv('DATABASE_URI')

# Create a new SQLAlchemy engine
engine = create_engine(database_uri)

# Create a new SQLAlchemy base class
Base = declarative_base()

# Define the Summary model
class Summary(Base):
    __tablename__ = 'summaries'

    id = Column(Integer, primary_key=True)
    summary = Column(String(5000))
    evaluation = Column(Integer)

# Create the table in the database
Base.metadata.create_all(engine)

# Create a new SQLAlchemy session
Session = sessionmaker(bind=engine)
session = Session()
