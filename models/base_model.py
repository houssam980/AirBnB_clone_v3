#!/usr/bin/python3
"""
Defines Base module
"""
from uuid import uuid4
from datetime import datetime
from models import storage


class BaseModel:
    """
    Define the BaseModel class
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize  BaseModel instance.

        Parameters
        args : arguments.
        kwargs : A key-worded arguments.
        """
        if (kwargs == {}):
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            for k, v in kwargs.items():
                if (k == "__class__"):
                    continue
                setattr(self, k, datetime.fromisoformat(v)
                        if ("_at" in k) else v)

    def __str__(self):
        """
        Return a string
        """
        return (f"[{type(self).__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """
        Updates attr
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Return dictionary of attributes
        """
        dict_obj = {}

        for k, v in self.__dict__.items():
            dict_obj[k] = v.isoformat() if ("_at" in k) else v
        dict_obj["__class__"] = type(self).__name__
        return (dict_obj)

