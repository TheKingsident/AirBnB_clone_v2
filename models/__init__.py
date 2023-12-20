#!/usr/bin/python3
""" Initialize the models package """
from os import getenv

# Env variable to determine the type of storage
storage_type = getenv('HBNB_TYPE_STORAGE')

if storage_type == 'db':
    # If storage type is 'db', use DBStorage
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    # If storage type is not 'db', use FilStorage
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

# Reload the storage, which is necessary for both DBStorage and FileStorage
storage.reload()
