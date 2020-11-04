#!/usr/bin/python3
"""On module load, create the storage variable"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
