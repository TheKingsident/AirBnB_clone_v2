#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
import models
from models.review import Review
from models.amenity import Amenity


from sqlalchemy import Table, Column, String, ForeignKey

# Define the association table for the many-to-many relationship
place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60), ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True, nullable=False),
                    extend_existing=True)


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []

    # Relationship with the Review class for DBStorage
    if models.storage_type == 'db':
        reviews = relationship("Review", backref="place",
                               cascade="all, delete")
        amenities = relationship("Amenity", secondary=place_amenity,
                                 viewonly=False)
    else:
        # Getter attribute reviews for FileStorage
        @property
        def reviews(self):
            """Returns the list of Review instances with place_id equals to
            the current Place.id"""
            from models.review import Review
            review_list = []
            all_reviews = models.storage.all(Review)
            for review in all_reviews.values():
                if review.place_id == self.id:
                    review_list.append(review)
            return review_list

        @property
        def amenities(self):
            """Returns the list of Amenity instances based on amenity_ids"""
            return [models.storage.get(Amenity, id) for id in self.amenity_ids]

        @amenities.setter
        def amenities(self, obj):
            """Adds an Amenity.id to amenity_ids"""
            if type(obj) == Amenity:
                self.amenity_ids.append(obj.id)
