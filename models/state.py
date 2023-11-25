#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
import os


class State(BaseModel, Base):
    """ State class """
    if storage_type == 'db':
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship('City', back_populates='state',
                              cascade="all, delete-orphan")
    else:
        name = ""

        @property
        def cities(self):
            """Getter attribute"""
            from models.city import City
            from models import storage
            # get all City instances
            res = []
            for city in storage.all(City).values():
                if city.state_id == self.id:
                    res.append(city)
            return res
