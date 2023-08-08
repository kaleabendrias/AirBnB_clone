#!/usr/bin/python3

"""
this is the basemodel for the airbnb console
"""
import uuid
import datetime
from . import storage


class BaseModel:
    """
    this class contains all attributes and methods
    that are needed as the base(class) for the airbnb console
    """

    def __init__(self, *args, **kwargs):
        """
        contain the attributes
        of objects
        """
        for key, value in kwargs.items():
            if key == "__class__":
                continue
            setattr(self, key, value)

        # checks if created_at has been passed to change to datetime object
        if hasattr(self, "created_at"):
            datetimeString = str(self.created_at)
            datetime_format = "%Y-%m-%d %H:%M:%S.%f"
            value = datetime.datetime.strptime(datetimeString, datetime_format)
            self.created_at = value

        # checks initialisation for these important attributes
        if not hasattr(self, "id"):
            self.id = str(uuid.uuid4())
        if not hasattr(self, "created_at"):
            self.created_at = datetime.datetime.now()

        self.updated_at = self.created_at

    def __str__(self):
        """
        output when object is printed out
        """
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """
        updates the time when
        the object instance is modified
        """
        storage.new(self)
        storage.save()
        self.updated_at = str(datetime.datetime.now().isoformat())

    def to_dict(self):
        """
        creates a dictionary
        of the attributes of an object
        also includes class name
        """
        objectDict = {}
        for key, value in self.__dict__.items():
            if isinstance(value, datetime.datetime):
                value = value.isoformat()
            objectDict[key] = value
        objectDict["__class__"] = self.__class__.__name__
        return (objectDict)
