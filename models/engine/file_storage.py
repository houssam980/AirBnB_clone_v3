#!/usr/bin/python3
"""
Defines module serialize and deserialize
instances.
"""
from json import dumps, loads
from os.path import isfile


class FileStorage:
    """
    Define mbbr for serializing instances
    """

    __file_path = "file.json"
    __objects = {}

    def all_obj(self):
        """ Return object"""
        return (FileStorage.__objects)

    def nw_obj(self, obj):
        """ set object value"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save_obj(self):
        """ save objects to a JSON file """
        objects = {}
        for k, v in FileStorage.__objects.items():
            objects[k] = v.to_dict()
        with open(FileStorage.__file_path, "w") as file:
            file.write(dumps(objects))

    def re_load(self):
        """ Deserializes the JSON file into object(s) """
        objects = {}

        if (isfile(FileStorage.__file_path)):
            with open(FileStorage.__file_path, "r") as file:
                objects = loads(file.read())
            from models.base_model import BaseModel
            from models.user import User
            from models.stt import State
            from models.ame import Ame
            from models.cty import Cty
            from models.plc import Plc
            from models.rev import Rev
            for key, value in objects.items():
                class_name = value["__class__"]
                del value["__class__"]
                FileStorage.__objects[key] = eval(class_name + "(**value)")

