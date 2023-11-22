#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship
from models import storage_type


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    if storage_type == 'db':
        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=False)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=False)
        longitude = Column(Float, nullable=False)
        amenity_ids = []

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
    def amenities(self):
        """returns review list instances with place_id equal to
        Place.id
        Will be the file storage rship between Place and Review
        """
        from models import storage
        all_amenitites = storage.all(Amenity)
        lst = []

        for amen_1 in all_amenities.values():
            if amen_1.id in self.amenity_ids:
                list.append(amen_1)
            return lst

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

    @amenities.setter(self, obj):
        if isinstance(obj, Amenity):
            if obj.id not in self.amenity_ids:
                self.amenity_ids.append(obj.id)
