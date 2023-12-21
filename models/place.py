#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base, String, Integer, Column
from sqlalchemy.orm import relationship
from sqlalchemy import Float, ForeignKey, Table


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(128))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, default=0)
    longitude = Column(Float, default=0)
    amenity_ids = []
    place_amenities = Table('place_amenity', Base.metadata,
                            Column('place_id', ForeignKey('places.id'),
                                   primary_key=True, nullable=False),
                            Column('amenity_id', ForeignKey('amenities.id'),
                                   primary_key=True, nullable=False))

    # table realationships

    cities = relationship("City", back_populates='places')
    users = relationship("User", back_populates='places')
    reviews = relationship("Review", back_populates='places',
                           cascade='all, delete-orphan')
    amenities = relationship("Amenity", secondary=place_amenities,
                             back_populates="places", viewonly=False)

    @property
    def amenities(self):
        """ retreives amenity instances """

        return self.amenities

    @amenities.setter
    def amenities(self, obj):
        """ Appends Amenity attributes to amenity_ids """

        if isinstance(obj, Amenity):
            self.amenity_ids.append(obj)
