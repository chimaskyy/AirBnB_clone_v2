#!/usr/bin/python3

from models.base_model import Base, BaseModel
import sqlalchemy
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, scoped_session
import os
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:
    """Database Storage System"""

    __engine = None
    __session = None
    classes = {
                    'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
              }

    def __init__(self):
        user = os.getenv('HBNB_MYSQL_USER')
        database = os.getenv('HBNB_MYSQL_DB')
        host = os.getenv('HBNB_MYSQL_HOST')
        password = os.getenv('HBNB_MYSQL_PWD')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            user, password, host, database), pool_pre_ping=True)

        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query all mapped classes if none is specified """

        all_objects = {}
        if not cls:
            for cls_ in self.classes.values():
                objs_tuple = self.__session.query(cls_).all()
                for obj in objs_tuple:
                    all_objects.update({obj.to_dict()['__class__'] + '.' +
                                       obj.id: obj})
        else:
            objs_tuple = self.__session.query(cls).all()

        # Iterates through all records in the table
            for obj in objs_tuple:
                all_objects.update({obj.to_dict()['__class__'] + '.' +
                                   obj.id: obj})

        return all_objects

    def new(self, obj):
        """Adds an object to the database in the current session"""

        self.__session.add(obj)

    def save(self):
        """Commits all changes made in the database"""

        self.__session.commit()

    def delete(self, obj=None):
        """deletes object from current session"""

        if obj:
            self.__session.delete(obj)

    def reload(self):
        """ creates all database tables """

        Base.metadata.create_all(self.__engine)

        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)

    def close(self):
        """closes current storage session."""

        self.__session.remove()
