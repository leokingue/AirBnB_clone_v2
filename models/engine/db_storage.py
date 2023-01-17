#!/usr/bin/python3
"""DBStorage Module"""
import models
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import sqlalchemy

classes = {"Amenity": Amenity, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class DBStorage:
    """DBStorage Class"""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a DBStorage object"""
        HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
        HBNB_ENV = getenv('HBNB_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
                                      HBNB_MYSQL_USER, HBNB_MYSQL_PWD,
                                      HBNB_MYSQL_HOST, HBNB_MYSQL_DB))
        
        if HBNB_ENV == "test":
            Base.metadata.drop_all(self.__engine)
    
    def all(self, cls=None):
        """query on the current database session
        all objects depending of the class name
        """
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    k = obj.__class__.__name__ + '.' + obj.id
                    new_dict[k] = obj
        return (new_dict)

     def new(self, obj):
         """add the object to the current database session"""
         self.__session.add(obj)

     def save(self):
         """commit all changes of the current database session"""
         self.__session.commit()

     def delete(self, obj=None):
         """delete from the current database session obj if not None"""
         if obj is not None:
             self.__session.delete(obj)

     def reload(self):
         """reload the database"""
         Base.metadata.create_all(self.__engine)
         s = sessionmaker(bind=self.__engine, expire_on_commit=False)
         Session = scoped_session(s)
         self.__session = Session

     def close(self):
         self.__session.remove()
