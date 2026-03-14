import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base
load_dotenv()
engine = create_engine(
        os.getenv("DBPath"), # type: ignore
        pool_pre_ping=True
    )
Session = sessionmaker(
        autocommit= False,
        autoflush=False,
        bind=engine
    )
Base = declarative_base()
def connectDB():
   db = Session()
   print("database connected")
   try:
    yield db
   finally:
    db.close()