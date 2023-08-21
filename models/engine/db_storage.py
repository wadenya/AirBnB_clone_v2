#!/usr/bin/python3
"""module defines DBStorage class"""
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


class DBStorage:
    """a class for Database storage"""
    __engine = None
    __session = None

    def __init__(self) -> None:
        """creates the engine"""
        self.__engine = create_engine()

