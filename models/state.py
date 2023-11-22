#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models import type_storage


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    if type_storage == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship("City", cascade="all, delete, delete-orphan",
                              backref="state")

    else:
        name = ""
        cities = ""
