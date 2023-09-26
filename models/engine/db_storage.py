#!/usr/bin/python3
"""module defines DBStorage class"""
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import relationship
from os import getenv

from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


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
        if cls is None:
            objs = self.__session.query(State).all()
            objs.extend(self.__session.query(City).all())
            objs.extend(self.__session.query(User).all())
            objs.extend(self.__session.query(Place).all())
            objs.extend(self.__session.query(Review).all())
            objs.extend(self.__session.query(Amenity).all())
        else:
            if type(cls) == str:
                cls = eval(cls)
            objs = self.__session.query(cls)
        return {"{}.{}".format(type(o).__name__, o.id): o for o in objs}

    def new(self, obj):
        """adds  object to db session"""
        self.__session.add(obj)

    def save(self):
        """commits all changes to db"""
        self.__session.commit()

    def delete(self, obj=None):
        """deletes object from db session if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """creates all tables in db"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Close thee running SQLAlchemy session."""
        self.__session.close()
