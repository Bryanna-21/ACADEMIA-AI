from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String)
    role = Column(String)  # admin, tutor, student

class ClassSession(Base):
    __tablename__ = "class_sessions"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    host_id = Column(Integer)
