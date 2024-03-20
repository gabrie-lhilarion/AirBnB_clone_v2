#!/usr/bin/python3

"""
Unit tests for the BaseModel class in the models.base_model module.
"""

from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models import storage
import unittest
import datetime
import json
import os
import subprocess
from shutil import copyfile


class test_basemodel(unittest.TestCase):
    """Test cases for the BaseModel class"""

    def __init__(self, *args, **kwargs):
        """Initializes the test case"""
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    @classmethod
    def setUpClass(cls):
        """Prepare environment for testing"""
        # Ensure file.json is in a known state or empty
        storage._FileStorage__objects = {}

    @classmethod
    def tearDownClass(cls):
        """Clean up after tests"""
        # Clear FileStorage objects to ensure a clean slate for other tests
        storage._FileStorage__objects = {}
        # Save the empty state to 'file.json' to cleanup
        storage.save()

    def test_default(self):
        """Test default instantiation of BaseModel"""
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """Test instantiation of BaseModel with keyword arguments"""
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """Test instantiation of BaseModel with invalid keyword arguments"""
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_save(self):
        """Test the save method of BaseModel"""
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_str(self):
        """Test the __str__ method of BaseModel"""
        i = self.value()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id,
                         i.__dict__))

    def test_todict(self):
        """Test the to_dict method of BaseModel"""
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        """Test instantiation of BaseModel with None as keyword argument"""
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_kwargs_one(self):
        """Test instantiation of BaseModel with one invalid keyword argument"""
        n = {'Name': 'test'}
        with self.assertRaises(KeyError):
            new = self.value(**n)

    def test_id(self):
        """Test the ID attribute of BaseModel"""
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """Test the created_at attribute of BaseModel"""
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """Test the updated_at attribute of BaseModel"""
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertFalse(new.created_at == new.updated_at)


if __name__ == '__main__':
    unittest.main()
