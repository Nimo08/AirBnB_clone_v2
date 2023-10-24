#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
import os


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    user = relationship('User', back_populates='places')
    cities = relationship('City', back_populates='places')

    storage_type = os.getenv('HBNB_TYPE_STORAGE')
    if storage_type == 'db':
        reviews = relationship('Review', back_populates='place',
                               cascade="all, delete-orphan")
    else:
        @property
        def reviews(self):
            """Getter attribute"""
            from models.place import Place
            from models import storage
            review_list = []
            for review in storage.all(Place).values():
                if review.place_id == self.id:
                    review_list.append(review)
            return review_list
