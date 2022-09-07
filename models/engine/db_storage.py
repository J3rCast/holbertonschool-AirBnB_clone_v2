#!/usr/bin/python3
"""This module defines a class to manage storage"""
from models.review import Review
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.state import State
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, Session, scoped_session
from os import getenv


class DBStorage():
    __engine = None
    __session = None

    def __init__(self):
        """Constructor method"""
        user = getenv('HBNB_MYSQL_USER')
        password = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        database = getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            user, password, host, database), pool_pre_ping=True)
        metadata_obj = MetaData()
        if getenv('HBNB_ENV') == 'test':
            metadata_obj.drop_all()

    def all(self, cls=None):
        """return a list of objects"""
        self.__session = Session(self.__engine)
        new_dict = {}
        if cls != None:
            for obj in self.__session.query(cls).all():
                new_dict.update({type(obj).__name__ + "." + obj.id: obj})
        else:
            classes = [User, State, City, Amenity, Place, Review]
            for i in classes:
                for obj in self.__session.query(i).all():
                    new_dict.update({type(obj).__name__ + "." + obj.id: obj})
        return new_dict

    def new(self, obj):
        """add new object"""
        self.__session.add(obj)

    def save(self):
        """Save the changes"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete an object"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """create tables based on database"""
        from models.base_model import Base
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=self.__session, expire_on_commit=False)
        Session = scoped_session(session)
        self.__session = Session()
