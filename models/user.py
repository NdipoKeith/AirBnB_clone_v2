#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'i

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)

    reviews = relationship("Review", backref="user", cascade="all,
                           delete-orphan")
    places = relationship("Place", backref="user", cascade="all,
                          delete-orphan")
