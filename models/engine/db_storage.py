#!/usr/bin/python3
"""This module defines a class to manage database storage for hbnb clone"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import urllib.parse

from models.base_model import BaseModel, Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place, place_amenity
from models.amenity import Amenity
from models.review import Review

class DBStorage():
    __engine = None
    __session = None

    def __init__(self):
        """initaializes SQL storage"""
        User = os.getenv('HBNB_MYSQL_USER')
        password = os.getenv('HBNB_MYSQL_PWD')
        host =os.getenv('HBNB_MYSQL_HOST')
        db_name = os.getenv('HBNB_MYSQL_DB')
        env = os.getenv('HBNB_ENV')

        DATABASE_URL = "mysql+mysqldb://{}:{}@{}:3306/{}".format(
            User, password, host, db_name
        )

        self.__engine = create_engine(
            DATABASE_URL, pool_pre_ping=True
        )
        if env == 'test':
            Base.metadata.drop_all(self.__engine)
    def all(self, cls=None):
        objects = dict()
        all_objects = (User, State, City, Amenity, Place, Review)
        if cls is None:
            for class_type in all_objects:
                query = self.__session.query(class_type)
                for obj in query.all():
                    obj_key = '{}.{}'.format(obj.__class__.__name__, obj.id)
                    objects[obj_key] = obj
        else:
            query = self.__session.query(cls)
            for obj in query.all():
                obj_key = '{}.{}'.format(obj.__class__.__name__, obj.id)
                objects[obj_key] = obj
        return objects
    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.query(type(obj)).filter(
                type(obj).id == obj.id).delete(
                    synchronize_sesion =False
            )

    def new(self, obj):
        """add the object to the current database session"""
        if obj is not None:
            try:
                self.__session.add(obj)
                self.__session.flush()
                self.__session.refresh(obj)
            except Exception as ex:
                self.__session.rollback()
                raise ex
    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()


    def reload(self):
        """create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        SessionFactory = sessionmaker(
            bind=self.__engine,
            expire_on_commit=False
        )
        self.__session = scoped_session(SessionFactory)

    


