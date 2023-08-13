#!/usr/bin/python3
"""
test for review module
"""
from models.review import Review
import unittest


class Test_Review(unittest.TestCase):
    """
    test for the review class
    """
    def test_for_doc(self):
        """
        tests if it has a documentation
        """
        self.assertIsNotNone(Review.__doc__)

    def test_for_place_id(self):
        """
        tests for the input of review_id
        """
        self.assertTrue(hasattr(Review, 'place_id'))
        self.assertIsInstance(Review.place_id, str)
        self.assertEqual(0, len(Review.place_id))

    def test_for_user_id(self):
        """
        tests for the input of user_id
        """
        self.assertTrue(hasattr(Review, 'user_id'))
        self.assertIsInstance(Review.user_id, str)
        self.assertEqual(0, len(Review.user_id))

    def test_for_text(self):
        """ test the attr text length """
        self.assertTrue(hasattr(Review, 'text'))
        self.assertIsInstance(Review.text, str)
        self.assertEqual(0, len(Review.text))
