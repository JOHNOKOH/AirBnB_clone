#!/usr/bin/python3
"""base_model module"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """Base class definition

    Attributes:
        id (string): Unique identifier
        created_at (datetime): date created
        updated_at (datetime): date updated

    """

    def __init__(self, *args, **kwargs):
        """Initializes a base model instance

        Args:
            *args (tuple): contains all arguments
            **kwargs (dictionary): contains all arguments by key/value
        """

        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)
        else:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.fromisoformat(value)
                if key != '__class__':
                    setattr(self, key, value)

    def __str__(self):
        """Returns class name, id and dictionary"""

        return f"[{self.__class__.__name__}] ({self.id}) {str(self.__dict__)}"

    def save(self):
        """Updates the pblic instance attribute updated_at"""

        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ returns a dictionary containing all keys/values
            of __dict__ of the instance:"""
        new_dict = {}
        for key, value in self.__dict__.items():
            if key == 'created_at' or key == 'updated_at':
                new_dict[key] = value.isoformat()
            else:
                new_dict[key] = value
        new_dict['__class__'] = self.__class__.__name__
        return new_dict
