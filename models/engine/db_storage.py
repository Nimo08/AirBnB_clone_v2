#!/usr/bin/python3
"""Database Storage"""

import os
from dotenv import load_dotenv
load_dotenv()
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


class DBStorage:
    """Defines DBStorage and its attributes"""
    __engine = None
    __session = None


    def __init__(self):
        env_var = os.getenv('HBNB_ENV')
        mysql_username = os.getenv('HBNB_MYSQL_USER')
        mysql_password = os.getenv('HBNB_MYSQL_PWD')
        mysql_host = os.getenv('HBNB_MYSQL_HOST')
        mysql_db = os.getenv('HBNB_MYSQL_DB')

        db_url = "mysql+mysqldb://{}:{}@{}/{}".format(mysql_username,
                                                      mysql_password, mysql_host, mysql_db)
        self.__engine = create_engine(db_url, pool_pre_ping=True)

        if env_var == "test":
            Base.metadata.drop_all()
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session_factory)


    def all(self, cls=None):
        """Query on the current database session"""
        from models.base_model import Base
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        if cls is None:
            classes = [User, State, City, Amenity, Place, Review]
        else:
            classes = [cls]
        result_dict = {}
        for class_model in classes:
            query = self.__session.query(table).all()
            for obj in query:
                key = f"{class_model.__name__}.{obj.id}"
                result_dict[key] = obj
        return result_dict

    def new(self, obj):
        """Add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """
        Create all tables in the database
        Create the current database session
        """
        from models.base_model import Base
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session_factory)
        


