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
    def __init__(self, *args, **kwargs):
        """ Method Dicription Here
        """

        if len(kwargs) != 0:
            for key, value in kwargs.items():
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
        """ Method Dicription Here
        """

        return "[{}] ({}) {}".\
            format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """ Method Dicription Here
        """

        self.update_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ Method Dicription Here
        """

        dictionary = self.__dict__.copy()
        dictionary["__class__"] = self.__class__.__name__
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()

        return dictionary
