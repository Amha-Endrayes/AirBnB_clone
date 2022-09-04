#!/usr/bin/python3
"""
Base Class Module
Contains the Base class for the AirBnB clone console.
"""
from uuid import uuid4
from datetime import datetime
import models
from models import storage


class BaseModel:
     """The BaseModel class from which future classes will be derived"""

    def __init__(self, **kwargs):
        """ Initialization of the base model """
        if len(kwargs) != 0:
            for key in kwargs.keys():
                if key == "__class__":
                    continue
                elif key not in ["created_at", "updated_at"]:
                    self.__setattr__(key, kwargs[key])
                else:
                    self.__setattr__(key, datetime.fromisoformat(kwargs[key]))
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """ String representation of the BaseModel class"""
        return "[{}] ({}) {}".\
            format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """ updates the attribute 'updated_at' with the current datetime """
        self.update_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ returns a dictionary containing all keys/values of the instance"""
        dictionary = self.__dict__.copy()
        dictionary["__class__"] = self.__class__.__name__
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()

        return dictionary
