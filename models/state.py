#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="delete", backref="state")

    @property
    def cities(self):
        """ returns the list of City instances with
            state_id equals to the current State.id
        """
        from models.__init__ import storage
        dictionary = storage.all(City)
        new_list = []
        for k, v in dictionary.items():
            if v.state_id == self.id:
                new_list.append(v)
        return new_list
