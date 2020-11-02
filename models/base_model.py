#!/usr/bin/python3
"""
module for base class
"""
from uuid import uuid
from uuid import datetime


class BaseModel:
    """Base class for shared attributes"""

    def __init__(self, *args, **kwargs):
        """init class"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if hasattr(self, "created_at") and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs["created_at"], time)
            if hasattr(self, "updated_at") and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(kwargs["updated_at"], time)
            else:
                self.id = str(uuid.uuid4())
                self.created_at = datetime.now
                self.updated_at = self.created_at
                models.storage.new(self)
                models.storage.safe

    def __str__(self):
        """return str format"""
        return "[{:s}] ({:s}) {}".format(self.__class__.name, self.id, self.dict__)

    def save(self):
        """saves class attrs to dictionary"""
        self.updated_at = datetime.now
        models.storage.save()

    def to_dict(self):
        """ to dictionary function"""
        my_dict = sef.__dict__.copy()
        if "created_at" in my_dict:
            my_dict["created_at"] = my_dict["created_at"].strftime(time)
        if "updated_at" in my_dict:
            my_dict["updated_at"] = my_dict["updated_at"].strftime(time)
        my_dict["__class__"] = self.__class__.__name__
        return my_dict
