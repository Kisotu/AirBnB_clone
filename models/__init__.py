#!/usr/bin/python3
'''creates a filestorage instance'''

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
