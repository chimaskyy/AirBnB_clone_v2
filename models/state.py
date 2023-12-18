#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base, String, Column
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", back_populates="states",
                          cascade='all, delete-orphan')
