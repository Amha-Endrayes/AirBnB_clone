#!/usr/bin/python3
""" Module Discription Here
"""
import json
import os
from models.base_model import BaseModel


class FileStorage:
    """ Class Discription
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Method Discription
        """
        return self.__objects

    def new(self, obj):
        """ Method Discription
        """
        new_key = f"{self.__name__}.{obj.id}"
        self.__dict_p.update(new_key=obj)

    def save(self):
        """ Method Discription
        """
        with open(FileStorage.__file_path, "w", encoding="utf-8") as jsonFile:
            s = {key: v.to_dict() for key, v in FileStorage.__objects.items()}
            json.dump(s, jsonFile)

    def reload(self):
        """ Method Discription
        """
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as jsonFile:
            obj_dict = json.load(jsonFile)
            obj_dict = {key: self.classes()[value["__class__"]](**value)
                        for key, value in obj_dict.items()}
            FileStorage.__objects = obj_dict
