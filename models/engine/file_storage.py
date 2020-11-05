#!/usr/bin/python3
"""This module holds the FileStorage class"""

import json
from os import path


class FileStorage():
    """Handles file storage"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the objects dictionary"""
        return FileStorage.__objects

    def new(self, obj):
        """Adds a new entry into the objects dictionary"""
        key = type(obj).__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """Saves the objects dictionary to file"""
        with open(FileStorage.__file_path, "w") as f:
            out = {}
            for k, v in FileStorage.__objects.items():
                out.update({k: v.to_dict()})
            f.write(json.dumps(out))

    def reload(self):
        """Reloads the objects dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        if path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as f:
                my_dict = json.loads(f.read())
                for k, v in my_dict.items():
                    myClass = eval(v["__class__"])
                    FileStorage.__objects[k] = myClass(**v)
