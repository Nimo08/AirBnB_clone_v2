#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, ForeignKey, Integer, Table
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = Table('place_amenities', Base.metadata,
                            Column('place_id', String(60),
                                   ForeignKey('places.id')),
                            Column('amenity_id', String(60),
                                   ForeignKey('amenities.id')))
