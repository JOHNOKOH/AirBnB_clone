#!/us/bin/python3
"""This is a module for filestorage class"""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """serializes instances to a JSON file
       and deserializes JSON files to instances

    Attributes:
        __objects (dict): store all objects by <class name>.id
        __file_path (str): path to the JSON file
    """

    __file_path = "hbnb.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id

        Args:

            obj (object): An instance object
        """
        FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """serializes __objects to the JSON file
           (path: __file_path)"""
        obj_dict = FileStorage.__objects
        serialized_obj = {key: obj.to_dict() for key, obj in obj_dict.items()}

        with open(FileStorage.__file_path, 'w') as f:
            json.dump(serialized_obj, f)

    def reload(self):
        """deserializes the JSON file to __ojects
        (only if the JSON file (__file_path) exists)"""

        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as f:
                deserialized_obj = json.load(f)
                for key, obj_data in deserialized_obj.items():
                    class_name, obj_id = key.split('.')
                    class_ = globals()[class_name]
                    obj = class_(**obj_data)
                    self.__objects[key] = obj

    def attributes(self):
        """This returns the valid attributes and their types for classname"""
        attributes = {
            "BaseModel":
                     {"id": str,
                      "created_at": datetime.datetime,
                      "updated_at": datetime.datetime},
            "User":
                     {"email": str,
                      "password": str,
                      "first_name": str,
                      "last_name": str},
            "State":
                     {"name": str},
            "City":
                     {"state_id": str,
                      "name": str},
            "Amenity":
                     {"name": str},
            "Place":
                     {"city_id": str,
                      "user_id": str,
                      "name": str,
                      "description": str,
                      "number_rooms": int,
                      "number_bathrooms": int,
                      "max_guest": int,
                      "price_by_night": int,
                      "latitude": float,
                      "longitude": float,
                      "amenity_ids": list},
            "Review":
            {"place_id": str,
                         "user_id": str,
                         "text": str}
        }
        return attributes
