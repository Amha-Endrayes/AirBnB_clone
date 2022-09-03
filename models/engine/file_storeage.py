#!/usr/bin/python3
"""
"""
import json
from models.base_model import BaseModel


class FileStorage:
    """
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        """
        return self.__objects

    def new(self, obj):
        """
        """
        new_key = f"{self.__name__}.{obj.id}"
        self.__dict_p.update(new_key=obj)

    def save(self):
        """
        """
        with open(__file_path, "w") as output:
            json.dump(_object, output)

    def reload(self):
        """
        """
        pass
