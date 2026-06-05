# from sqlmodel import Field, Session, SQLModel, create_engine, select
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine import URL
import psycopg
from psycopg.rows import dict_row
from .config import settings



SQLALCHEMY_DATABASE_URL = (
    f"postgresql+psycopg://{settings.database_username}:"
    f"{settings.database_password}@{settings.database_hostname}:"
    f"{settings.database_port}/{settings.database_name}"
)

# SQLALCHEMY_DATABASE_URL = "postgresql+psycopg://postgres:postgres@localhost/fastapi"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# try:
#     conn = psycopg.connect(host='127.0.0.1', dbname='fastapi', user='postgres', password='Kusal@1904', row_factory=dict_row)
#     cursor = conn.cursor()
#     print("Database connection was successful!")
# except Exception as error:
#     print("Database connection failed!")
#     print("Error: ", error)
#     time.sleep(2) 