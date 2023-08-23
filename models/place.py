#!/usr/bin/python3
""" Place Module for HBNB project """
from models.amenity import Amenity
from models.review import Review
from models import storage
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.sql.schema import Table
from sqlalchemy.orm import relationship


# Define place_amenity table for Many-To-Many relationship
place_amenity = Table('place_amenity', Base.metadata,
                          Column('place_id', String(60),
                                 ForeignKey('places.id'),
                                 primary_key=True, nullable=False),
                          Column('amenity_id', String(60),
                                 ForeignKey('amenities.id'),
                                 primary_key=True, nullable=False))

class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places';
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    reviews = relationship('Review', backref='place',
                               cascade='delete')
    amenities = relationship('Amenity', secondary=place_amenity,
                                viewonly=False, backref='place_amenities')
    amenity_ids = []

    @property
    def reviews(self):
    '''Return list of reviews associated with this Place.'''
    all_reviews = storage.all(Review)
    review_list = []
    for review_instance in all_reviews.values():
        if review_instance.place_id == self.id:
            review_list.append(review_instance)
    return review_list

    @property
    def amenities(self):
    '''Return list of Amenity instances linked to this Place.'''
    all_amenities = storage.all(Amenity)
    amenities_list = []
    for amenity_instance in all_amenities.values():
        if amenity_instance.id in self.amenity_ids:
            amenities_list.append(amenity_instance)
    return amenities_list

    @amenities.setter
    def amenities(self, amenity_obj):
    '''
    Add an Amenity ID to amenity_ids if it's a valid Amenity instance.
    '''
    if amenity_obj is not None:
        if isinstance(amenity_obj, Amenity):
            if amenity_obj.id not in self.amenity_ids:
                self.amenity_ids.append(amenity_obj.id)
