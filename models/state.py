#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy import relationship

class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete", backref="state"
