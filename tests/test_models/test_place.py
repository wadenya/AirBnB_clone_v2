#!/usr/bin/python3
"""test place"""
import os
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """clss test place"""

    def __init__(self, *args, **kwargs):
        """init test clss """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """test city id """
        new = self.value()
        self.assertEqual(type(new.city_id), str if
                        os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                        type(None))

    def test_user_id(self):
        """test user id """
        new = self.value()
        self.assertEqual(type(new.user_id), str if
                        os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                        type(None))

    def test_name(self):
        """test plc name """
        new = self.value()
        self.assertEqual(type(new.name), str if
                        os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                        type(None))

    def test_description(self):
        """test plc descrip """
        new = self.value()
        self.assertEqual(type(new.description), str if
                os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                type(None))

    def test_number_rooms(self):
        """test number of rooms """
        new = self.value()
        self.assertEqual(type(new.number_rooms), int if
                        os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                        type(None))

    def test_number_bathrooms(self):
        """test numb of bathrms """
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int if
                        os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                        type(None))

    def test_max_guest(self):
        """test max guest of place"""
        new = self.value()
        self.assertEqual(type(new.max_guest), int if
                        os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                        type(None))

    def test_price_by_night(self):
        """test price by nght of plc"""
        new = self.value()
        self.assertEqual(type(new.price_by_night), int if
                        os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                        type(None))

    def test_latitude(self):
        """test lat of place """
        new = self.value()
        self.assertEqual(type(new.latitude), float if
                        os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                        type(None))

    def test_longitude(self):
        """test long of place"""
        new = self.value()
        self.assertEqual(type(new.latitude), float if
                        os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                        type(None))

    def test_amenity_ids(self):
        """test amenity of place"""
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list if
                        os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                        type(None))
