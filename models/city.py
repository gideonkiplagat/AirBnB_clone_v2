#!/usr/bin/python3
""" City Module for HBNB project """
from sqlalchemy import Column, String, Foreignkey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base

import os


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    name = Column(
        String(128), nullable=False
    ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''
    state_id = Column(
        String(60), Foreignkey('states.id'), nullable=False
    ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''
    places = relationship(
        'place',
        cascade='all, delete, delete-orphan',
        back_populates='cities'
    ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else None
