#!/usr/bin/python3
"""
module for base class
"""
import uuid
from datetime import datetime

class BaseModel:
    """Base class for shared attributes"""

    from models.__init__ import storage
    def __init__(self, *args, **kwargs):
        """init class"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if hasattr(self, "created_at") and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
            if hasattr(self, "updated_at") and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)
#            models.storage.safe

    def __setattr__(self, name, value):
        """x"""
        self.__dict__["updated_at"] = datetime.now()
        self.__dict__[name] = value

    def __str__(self):
        """return str format"""
        return "[{:s}] ({:s}) {}".format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """saves class attrs to dictionary"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """ to dictionary function"""
        my_dict = self.__dict__.copy()
        if "created_at" in my_dict:
            my_dict["created_at"] = my_dict["created_at"].strftime("%Y-%m-%dT%H:%M:%S.%f")
        if "updated_at" in my_dict:
            my_dict["updated_at"] = my_dict["updated_at"].strftime("%Y-%m-%dT%H:%M:%S.%f")
        my_dict["__class__"] = type(self).__name__
        return my_dict
