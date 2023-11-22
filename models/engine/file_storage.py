#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'

    def __init__(self):
        self.__objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls is None:
            return self.__objects
        else:
            return [obj for obj in self.__objects if isinstance(obj, cls)]

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        self.__objects.clear()

        try:
            temp = self.__objects.copy()
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                """
                for key, val in temp.items():
                        self.__objects()[key] =
                        classes[val['__class__']](**val)
                        """
                self.__objects = {key: classes[val['__class__']](**val)
                                  for key, val in temp.items()}
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """method to delete object from _objects"""
        if obj is not None and obj in self.__objects:
            del self.__objects[obj]
            """
            temp_objects = self.__objects.copy()
            temp_objects.remove(obj)
            self.__objects = temp_objects
            """
