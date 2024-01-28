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

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City", back_populates="states",
                              cascade='all, delete-orphan')
    else:
        @property
        def cities(self):
            """Fetches list of all related City objects to state instance."""
            from models import storage

            state_cities = []
            for city in storage.all(City).values():
                if hasattr(city, 'state_id') and city.state_id == self.id:
                    state_cities.append(city)
            return state_cities
