from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base

import os


URL_DATABASE = os.getenv("URL_DATABASE")

if not URL_DATABASE:
    raise ValueError("DATABASE_URL environment variable not set")

engine = create_engine(URL_DATABASE)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

