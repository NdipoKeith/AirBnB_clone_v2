#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'
    if type_storage == "db":
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=False)
        last_name = Column(String(128), nullable=False)
        reviews = relationship("Review", backref="user", cascade="all,
                               delete, delete-orphan")
        places = relationship("Place", backref="user", cascade="all,
                              delete, delete-orphan")

    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""
