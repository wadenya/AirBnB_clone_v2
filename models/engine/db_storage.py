#!/usr/bin/python3
"""module defines DBStorage class"""
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from os import getenv

from models.base_model import BaseModel, Base


class DBStorage:
    """a class for Database storage"""
    __engine = None
    __session = None

    def __init__(self) -> None:
        """creates the engine"""
        conn_str = 'mysql+mysqldb://{}:{}@{}/{}'.format(
            getenv('HBNB_MYSQL_USER'),
            getenv('HBNB_MYSQL_PWD'),
            getenv('HBNB_MYSQL_HOST'),
            getenv('HBNB_MYSQL_DB'))
        self.__engine = create_engine(conn_str, pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """get all objects in db based on cls"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        if cls is not None:
            objs = {}
            objs[cls] = self.__session.query(classes[cls]).all()
        else:
            for _cls in classes:
                objs = {}
                objs[_cls] = self.__session.query(classes[_cls]).all()
        return {"{}.{}".format(type(obj).__name__, obj.id): obj for obj in objs}