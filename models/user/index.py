from sqlalchemy import Column,String
from database.index import Base


class User(Base):
    __tablename__="users"
    id=Column(String(255),primary_key=True)
    name=Column(String(255))
    email=Column(String(255),unique=True,index=True)
    password = Column(String(255))