#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from models import storage
from models.city import City
import os


Base = declarative_base()


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    
    storage_type = os.getenv('HBNB_TYPE_STORAGE')
    if storage_type == 'db':
        cities = relationship("City", back_populates="state",
                          cascade="all, delete-orphan")
    else:
        @property
        def cities(self):
            """Getter attribute"""
            from models.city import City
            # get all City instances
            res = []
            for city in storage.all(City).values():
                if city.state_id == state.id:
                    res.append(city)
            return res
