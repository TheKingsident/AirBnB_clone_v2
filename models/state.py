#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    # Relationship with the City class for DBStorage
    # Getter attribute cities for FileStorage

    @property
    def cities(self):
        """Returns the list of City instances with state_id equals to
        the current State.id"""
        from models.city import City
        import models

        if getattr(models, 'storage', None) == 'db':
            return relationship("City", backref="state", cascade="all, delete")
        else:
            city_list = []
            all_cities = models.storage.all(City)
            for city in all_cities.values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
