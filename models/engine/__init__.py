#!/usr/bin/python3
"""Add a conditional depending of the value of the environment variable """
import os

from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage

storage = DBStorage() if os.getenv(
    'HBNB_TYPE_STORAGE') == 'db' else FileStorage()
"""Create an instance of FileStorage and store it in the variable storage"""
storage.reload()
