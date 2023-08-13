#!/usr/bin/python3
"""
test for place module
"""
from models.place import Place
import unittest


class Test_Place(unittest.TestCase):
    """
    test for the place class
    """
    def test_for_doc(self):
        """
        tests if it has a documentation
        """
        self.assertIsNotNone(Place.__doc__)

    def test_for_city_id(self):
        """
        tests for the input of city_id
        """
        self.assertTrue(hasattr(Place, 'city_id'))
        self.assertIsInstance(Place.city_id, str)
        self.assertEqual(0, len(Place.city_id))

    def test_for_user_id(self):
        """
        tests for the input of user_id
        """
        self.assertTrue(hasattr(Place, 'user_id'))
        self.assertIsInstance(Place.user_id, str)
        self.assertEqual(0, len(Place.user_id))

    def test_for_name(self):
        """ test the attr name length """
        self.assertTrue(hasattr(Place, 'name'))
        self.assertIsInstance(Place.name, str)
        self.assertEqual(0, len(Place.name))

    def test_for_description(self):
        """ test the attr description """
        self.assertTrue(hasattr(Place, 'description'))
        self.assertIsInstance(Place.description, str)
        self.assertEqual(0, len(Place.description))

    def test_for_number_rooms(self):
        """ tests for the number of rooms """
        self.assertTrue(hasattr(Place, 'number_rooms'))
        self.assertEqual(0, Place.number_rooms)
        self.assertIsInstance(Place.number_rooms, int)

    def test_for_number_bathrooms(self):
        """ tests for the number of bathrooms """
        self.assertTrue(hasattr(Place, 'number_bathrooms'))
        self.assertEqual(0, Place.number_bathrooms)
        self.assertIsInstance(Place.number_bathrooms, int)

    def test_for_max_guest(self):
        """ tests for the max guests """
        self.assertTrue(hasattr(Place, 'max_guest'))
        self.assertEqual(0, Place.max_guest)
        self.assertIsInstance(Place.max_guest, int)

    def test_for_price_by_night(self):
        """ tests for the price by night """
        self.assertTrue(hasattr(Place, 'price_by_night'))
        self.assertEqual(0, Place.price_by_night)
        self.assertIsInstance(Place.price_by_night, int)

    def test_for_latitude(self):
        """ tests for the latitude """
        self.assertTrue(hasattr(Place, 'latitude'))
        self.assertEqual(0.0, Place.latitude)
        self.assertIsInstance(Place.latitude, float)

    def test_for_longitude(self):
        """ tests for the longitude """
        self.assertTrue(hasattr(Place, 'longitude'))
        self.assertEqual(0.0, Place.longitude)
        self.assertIsInstance(Place.longitude, float)

    def test_for_amenity_ids(self):
        """
        tests the ids for the amenities provided
        """
        self.assertTrue(hasattr(Place, 'amenity_ids'))
        self.assertEqual([], Place.amenity_ids)
        self.assertIsInstance(Place.amenity_ids, list)
