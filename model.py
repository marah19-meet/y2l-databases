from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine


Base = declarative_base()

class Student(Base):
   __tablename__='Table'
   id=Column(Integer,primary_key=True)
   product=Column(String)
   price=Column(Integer)
   quantity=Column(Integer)
   description=Column(String)

  
