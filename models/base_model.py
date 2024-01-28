#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, DateTime

Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""
    id = Column(String(60), default=str(uuid.uuid4()), primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow(), nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow(), nullable=False)

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if kwargs:
            # sets attribute from dictionary
            if '__class__' in kwargs:
                del kwargs['__class__']
            for k, v in kwargs.items():
                if k in ('updated_at', 'created_at'):
                    setattr(self, k, datetime.fromisoformat(v))
                else:
                    setattr(self, k, v)
            if 'id' not in kwargs:
                setattr(self, 'id', str(uuid.uuid4()))
            if 'created_at' not in kwargs:
                setattr(self, 'created_at', datetime.utcnow())
            if 'updated_at' not in kwargs:
                setattr(self, 'updated_at', datetime.utcnow())
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = self.__class__.__name__
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.utcnow()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        for k, v in self.__dict__.items():
            if isinstance(v, datetime):
                dictionary[k] = v.isoformat()
            else:
                dictionary[k] = v
        if '_sa_instance_state' in dictionary:
            del dictionary['_sa_instance_state']
        return dictionary

    def delete(self):
        """Deletes the current instance from storage"""

        from models import storage
        storage.delete(self)
