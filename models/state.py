#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base, String, Column
from sqlalchemy.orm import relationship
from os import getenv
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    # check if storage type is db
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        '''Define a relationship between State and City models.
        This defines a one-to-many relationship where one State
        can have multiple associated City objects.
        The back_populates parameter specifies the name of
        the attribute on the City model that will be used to access
        the related State object.The cascade parameter specifies
        that when a State object is deleted, all associated
        City objects should also be deleted'''
        cities = relationship("City", back_populates="states",
                              cascade='all, delete-orphan')
    else:
        @property
        def cities(self):
            """Fetches list of all related City
            objects to current state instance."""
            from models import storage

            state_cities = []
            # iterate over all city obj stored in storage file
            for city in storage.all(City).values():
                '''Check if the city object has a 'state_id'
                attribute and if its value matches the id of
                the current State instance'''
                if hasattr(city, 'state_id') and city.state_id == self.id:
                    state_cities.append(city)
            return state_cities
