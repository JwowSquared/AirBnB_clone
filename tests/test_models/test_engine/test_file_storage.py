#!/usr/bin/python3
"""this is essentially a file cabinet"""
import unittest
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """You remember what manilla folders look like? me neither"""
    def test_blank(self):
        """I always thought it was vanilla folders like there were flavour variants"""
        self.assertEqual(1, 1)
