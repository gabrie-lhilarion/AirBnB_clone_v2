from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
import uuid
import models

time_format = "%Y-%m-%dT%H:%M:%S.%f"
Base = declarative_base()

class BaseModel(Base):

    """The BaseModel class from which future classes will be derived"""
    __abstract__ = True
    
    def __init__(self, *args, **kwargs):
        """Initialization of the base model"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if kwargs.get("created_at", None) and isinstance(self.created_at, str):
                self.created_at = datetime.strptime(kwargs["created_at"], time_format)
            else:
                self.created_at = datetime.utcnow()
            if kwargs.get("updated_at", None) and isinstance(self.updated_at, str):
                self.updated_at = datetime.strptime(kwargs["updated_at"], time_format)
            else:
                self.updated_at = datetime.utcnow()
            if kwargs.get("id", None) is None:
                self.id = str(uuid.uuid4())
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = self.created_at

    def __str__(self):
        """String representation of the BaseModel class"""
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id,
                                         self.__dict__)

    def save(self):
        """updates the attribute 'updated_at' with the current datetime"""
        self.updated_at = datetime.utcnow()
        if models.storage_t == "db":
            models.storage.new(self)
            models.storage.save()
        elif models.storage_t == "file":
            models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of the instance"""
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        for attr_name in ["created_at", "updated_at"]:
            if attr_name in new_dict:
                new_dict[attr_name] = new_dict[attr_name].strftime(time_format)
        return new_dict

    def delete(self):
        """delete the current instance from the storage"""
        models.storage.delete(self)
