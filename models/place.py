#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship
from models import storage_type
from models.amenity import Amenity
from models.review import Review
from sqlalchemy.sql.schema import Table


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    if storage_type == 'db':
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

    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = ""
        number_bathrooms = ""
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

    @property
    def reviews(self):
        """returns list of amenity instance based on id contsined"""
        from models import storage
        all_reviews = storage.all(Review)
        rev_lst = []

        for rev in all_reviews.values():
            if rev.place_id == self.id:
                rev_lst.append(rev)
        return rev_lst

    @property
    def amenitites(self):
        """returns a list of amenities associated with a place"""
        from models import storage
        all_amenities = storage.all(Amenity)
        amen_list = []

        for amen in all_amenities.values():
            if amen.id in self.amenity_ids:
                amen_llist.append(amen)
        return aamen_list

    def amenities(self, obj):
        """adds or removes an amenity from the place"""
        if obj is not None:
            if isinstance(obj, Amenity):
                self.amenity_ids.append(obj.id)
