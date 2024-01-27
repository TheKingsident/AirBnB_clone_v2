#!/usr/bin/python3
""" DBStorage engine """
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from os import getenv
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review


class DBStorage:
    """This class manages storage of hbnb models in a MySQL database"""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a DBStorage object"""
        default_user = 'hbnb_dev'
        default_pwd = 'hbnb_dev_pwd'
        default_host = 'localhost'
        default_db = 'hbnb_dev_db'

        user = getenv('HBNB_MYSQL_USER', default_user)
        pwd = getenv('HBNB_MYSQL_PWD', default_pwd)
        host = getenv('HBNB_MYSQL_HOST', default_host)
        db = getenv('HBNB_MYSQL_DB', default_db)
        self.__engine = create_engine(
            f'mysql+mysqldb://{user}:{pwd}@{host}/{db}', pool_pre_ping=True)

        if getenv('HBNB_ENV') == 'test':
            # Drop all tables for testing environment
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query all objects of a given class from the dbase
        or all classes if cls is None"""
        all_objs = {}
        if cls:
            objs = self.__session.query(cls).all()
            for obj in objs:
                key = f'{obj.__class__.__name__}.{obj.id}'
                all_objs[key] = obj
        else:
            pass
        return all_objs

    def new(self, obj):
        """Add an object to the current dbase session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current dbase session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete an object from the current dbase session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the dbase and the current dbase session"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Closes the session"""
        if isinstance(self.__session, scoped_session):
            self.__session.remove()
        else:
            self.__session.close()
