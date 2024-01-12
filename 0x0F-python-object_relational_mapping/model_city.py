#!/usr/bin/python3
"""Write a Python file similar to model_state.py named
model_city.py that contains the class definition of a City."""
from model_state import Base
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base

class City(Base):

    __tablename__ = 'cities'
     id = Column(Integer, unique=True, nullable=False, primary_key=True)
     name = Column(String(128), nullable=False)
     state_id = Column(Integer, nullable=False, ForeignKey("states.id"))