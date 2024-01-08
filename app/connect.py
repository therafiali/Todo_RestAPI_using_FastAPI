from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os
from sqlalchemy.orm import DeclarativeBase

load_dotenv()

key = os.getenv("db_key")

SQLALCHEMY_DATABASE_URL = f'{key}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

 