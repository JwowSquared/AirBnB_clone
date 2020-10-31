#!/usr/bin/python3
"""x"""

import json
from os import path

class FileStorage():
    """x"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """x"""
        return FileStorage.__objects

    def new(self, obj):
        """x"""
        key = type(obj).__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """x"""
        with open(FileStorage.__file_path, "w") as f:
            out = {}
            for k, v in FileStorage.__objects.items():
                out[k] = v.to_dict()
            f.write(json.dumps(out))

    def reload(self):
        """x"""
        from models.base_model import BaseModel
        if path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as f:
                my_dict = json.loads(f.read())
                for k, v in my_dict.items():
                    FileStorage.__objects[k] = BaseModel(v)


