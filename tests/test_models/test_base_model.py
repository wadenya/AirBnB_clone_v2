#!/usr/bin/python3
"""test base model"""
from models.base_model import BaseModel
import unittest
import datetime
from uuid import UUID
import json
import os

@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db',
                 'basemodel test not supported')
class test_basemodel(unittest.TestCase):
    """class test basemodel"""

    def __init__(self, *args, **kwargs):
        """init"""
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """test class setup method"""
        pass

    def tearDown(self):
        try:
            os.remove('file.json')
        except:
            pass

    def test_default(self):
        """test default"""
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """test kwargs"""
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """test kwargs int"""
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_save(self):
        """ Testing save """
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_str(self):
        """test for string"""
        i = self.value()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id,
                         i.__dict__))

    def test_todict(self):
        """test to dictionry meth"""
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)
        self.assertIsInstance(self.value().to_dict(), dict)
        self.assertIn('id', self.value().to_dict())
        self.assertIn('created_at', self.value().to_dict())
        self.assertIn('updated_at', self.value().to_dict())

        user_obj = self.value()
        user_obj.firstname = 'Eleanor'
        user_obj.lastname = 'Rigby'
        self.assertIn('firstname', user_obj.to_dict())
        self.assertIn('lastname', user_obj.to_dict())
        self.assertIn('firstname', self.value(firstname='Eleanor').to_dict())
        self.assertIn('lastname', self.value(lastname='Rigby').to_dict())

        self.assertIsInstance(self.value().to_dict()['created_at'], str)
        self.assertIsInstance(self.value().to_dict()['updated_at'], str)

        datetime_now = datetime.today()
        user_obj = self.value()
        user_obj.id = '567890'
        user_obj.created_at = user_obj.updated_at = datetime_now
        to_dict = {
            'id': '567890',
            '__class__': user_obj.__class__.__name__,
            'created_at': datetime_now.isoformat(),
            'updated_at': datetime_now.isoformat()
        }
        self.assertDictEqual(user_obj.to_dict(), to_dict)
        if os.getenv('HBNB_TYPE_STORAGE') != 'db':
            self.assertDictEqual(
                self.value(id='u-b34', age=25).to_dict(),
                {
                    '__class__': user_obj.__class__.__name__,
                    'id': 'u-b34',
                    'age': 25
                }
            )
            self.assertDictEqual(
                self.value(id='u-b34', age=None).to_dict(),
                {
                    '__class__': user_obj.__class__.__name__,
                    'id': 'u-b34',
                    'age': None
                }
            )
        user_obj_d = self.value()
        self.assertIn('__class__', self.value().to_dict())
        self.assertNotIn('__class__', self.value().__dict__)
        self.assertNotEqual(user_obj_d.to_dict(), user_obj_d.__dict__)
        self.assertNotEqual(
            user_obj_d.to_dict()['__class__'],
            user_obj_d.__class__
        )

        with self.assertRaises(TypeError):
            self.value().to_dict(None)
        with self.assertRaises(TypeError):
            self.value().to_dict(self.value())
        with self.assertRaises(TypeError):
            self.value().to_dict(45)
        self.assertNotIn('_sa_instance_state', n)


    def test_kwargs_none(self):
        """test kwargs with no args"""
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_kwargs_one(self):
        """test kwargs with one arg"""
        n = {'Name': 'test'}
        with self.assertRaises(KeyError):
            new = self.value(**n)

    def test_id(self):
        """test id """
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """test created at"""
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """test update at"""
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertFalse(new.created_at == new.updated_at)
