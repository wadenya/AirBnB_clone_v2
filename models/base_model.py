#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class BaseModel:
    """A base class for all hbnb models"""

    id = Column(
        String(60),
        unique=True,
        nullable=False,
        primary_key=True)
    created_at = Column(
        DateTime,
        nullable=False,
        default=datetime.utcnow)
    updated_at = Column(
        DateTime,
        nullable=False,
        default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    setattr(self, k, datetime.fromisoformat(v))
                elif k != "__class__":
                    setattr(self, k, v)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        _dict = {}
        keys = self.__dict__.keys()
        for key in keys:
            if key != '_sa_instance_state':
                _dict[key] = self.__dict__[key]
        _dict['__class__'] = self.__class__.__name__
        _dict['created_at'] = self.created_at.isoformat()
        _dict['updated_at'] = self.updated_at.isoformat()
        print("dict: ")
        print(_dict)
        return _dict
    
    
    def delete(self):
        """del instance from storage"""
        from models import storage
        storage.delete(self)
