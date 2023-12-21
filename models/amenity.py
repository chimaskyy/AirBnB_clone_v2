#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Column, Base, String
from sqlalchemy import Table, ForeignKey
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """ Amenity class """
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary='place_amenity',
                                   back_populates='amenities')
    places = place_amenities
