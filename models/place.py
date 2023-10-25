#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session
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
    place_amenity = Table('place_amenity', Base.metadata,
                          Column('place_id', String(60),
                                 ForeignKey('places.id'), primary_key=True,
                                 nullable=False),
                          Column('amenity_id', String(60),
                                 ForeignKey('amenities.id'), primary_key=True,
                                 nullable=False))

    storage_type = os.getenv('HBNB_TYPE_STORAGE')
    if storage_type == 'db':
        reviews = relationship('Review', back_populates='place',
                               cascade="all, delete-orphan")
        amenities = relationship('Amenity', secondary=place_amenity,
                                 viewonly=False)
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

        @property
        def amenities(self):
            """Getter attribute"""
            query = session.query(Amenity).filter(Amenity.id.in_
                                                  (self.amenity_ids)).all()
            return query

        @amenities.setter
        def amenities(self, amenity):
            """Setter attribute"""
            if isinstance(amenity, Amenity):
                self.amenity_ids.append(amenity.id)
            else:
                pass
