#!/usr/bin/python3
"""
Base Class Module
Contains the Base class for the AirBnB clone console.
"""

from uuid import uuid4
from datetime import datetime
from models.base_model import BaseModel
from models import storage


class BaseModel:
    def __init__(self, *args, **kwargs):
        """
        """
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "updated_at" or key == "created_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    setattr(self, key, value)
                setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """
        """
        return "[{}] ({}) {}".\
            format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """
        """
        self.update_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        """
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__': (type(self).__name__)})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()

        return dictionary
