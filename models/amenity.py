#!/usr/bin/python3
""" Amenity module for the HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Table, Column, String, ForeignKey


class Amenity(BaseModel, Base):
    """ Amenity class for HBNB project """
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
