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
        FileStorage.__objects[key] = obj.to_dict()

    def save(self):
        """x"""
        with open(FileStorage.__file_path, "w") as f:
            f.write(json.dumps(FileStorage.__objects))

    def reload(self):
        """x"""
        if path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as f:
                FileStorage.__objects = json.loads(f.read())
