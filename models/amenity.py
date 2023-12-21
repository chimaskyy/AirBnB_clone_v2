#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Column, Base, String
from sqlalchemy import Table, ForeignKey
from models.place import Place
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """ Amenity class """
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary=Place.place_amenities)
