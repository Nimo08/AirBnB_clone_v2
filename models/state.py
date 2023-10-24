#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
import os


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    storage_type = os.getenv('HBNB_TYPE_STORAGE')
    if storage_type == 'db':
        cities = relationship("City", back_populates="state",
                              cascade="all, delete-orphan")
    else:
        pass
