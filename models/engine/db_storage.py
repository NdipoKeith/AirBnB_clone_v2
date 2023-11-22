#!/usr/bin/python3

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base


class DBStorage:

    __engine = None
    __session = None

    def __init__(self):
        user = os.getenv("HBNB_MYSQL_USER")
        passwd = os.getenv("HBNB_MYSQL_PWD")
        host = os.genenv("HBNB_MYSQL_HOST")
        database = os.getenv("HBNB_MYSQL_DB")

        self.__engine = ("mysql+mysqldb://{}:{}@{}:3306/{}".format(
            user, passwd, host, database), pool_pre_ping=True)

        if env == "test":
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        obj_dict = {}
        classes = [User, State, City, Place, Reeview]

        if cls:
            classes = [cls]
        for cls in classes:
            objs = self.__session.query(cls).all()
            for obj in objs:
                key = "{}.{}".fomat(obj.__class__.__name__, obj.id)
                obj_dict[key] = obj
        return obj_dict

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj:
            self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        Base.metadata.bind = self.__engine
        session = sessionmaker(bind=self.__engine)
        Session = scoped_session(session)
        self.__session = Session
