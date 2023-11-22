#!/usr/bin/python3

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.amenity import Amenity
from models.city import City
from models.user import User
from models.review import Review
from models.state import State
from models.place import Place

classes = {"User": User, "State": State, "City": City, "Amenity": Amenity,
           "Place": Place, "Review": Review}


class DBStorage:
    """private class attributes"""

    __engine = None
    __session = None

    def __init__(self):
        """instantiate class DBStorage"""
        user = os.getenv("HBNB_MYSQL_USER")
        passwd = os.getenv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST")
        database = os.getenv("HBNB_MYSQL_DB")
        env = os.getenv("HBNB_ENV")

        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".format(
            user, passwd, host, database), pool_pre_ping=True)

        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        obj_dict = {}
        classes = [User, State, City, Place, Review]

        if cls:
            classes = [cls]
        for cls in classes:
            objs = self.__session.query(cls).all()
            for obj in objs:
                key = "{}.{}".fomat(obj.__class__.__name__, obj.id)
                obj_dict[key] = obj
        return obj_dict

    def new(self, obj):
        """add object to db session"""
        if obj is not None:
            try:
                self.__session.add(obj)
                self.__session.flush()
                self.__session.refresh(obj)
            except:
                self.__session.rollback()
                raise ex

    def save(self):
        """commit changes to db session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete obj from db session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        Base.metadata.bind = self.__engine
        session = sessionmaker(bind=self.__engine)
        Session = scoped_session(session)
        self.__session = Session

    def close(self):
        """close session"""
        self.__session.close()
