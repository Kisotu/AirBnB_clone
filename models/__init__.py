#!/usr/bin/python3
'''creates a filestorage instance'''

from .engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
