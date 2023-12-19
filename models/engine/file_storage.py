#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}
    classes = {
                'BaseModel': BaseModel, 'User': User, 'Place': Place,
                'State': State, 'City': City, 'Amenity': Amenity,
                'Review': Review
              }

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""

        if not cls:
            return FileStorage.__objects

        cls_dict = {}
        for k, v in FileStorage.__objects.items():
            if cls.__name__ in k:
                cls_dict.update({k: v.to_dict()})

        return cls_dict

    def new(self, obj):
        """Adds new object to storage dictionary"""
        key = obj.__class__.__name__ + '.' + obj.id
        FileStorage.__objects[key] = obj

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

        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = self.classes[val['__class__']](**val)
        except Exception:
            pass

    def delete(self, obj=None):
        """Deletes and Object from storage"""

        if obj:
            obj_key = obj.to_dict()['__class__'] + '.' + obj.id
            if obj_key in FileStorage.__objects.keys():
                del FileStorage.__objects[obj_key]
