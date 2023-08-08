#!/usr/bin/python3

"""
creates an instance of FileStorage
"""

from .engine.file_storage import FileStorage

storage = FileStorage()
storage.reload() 
