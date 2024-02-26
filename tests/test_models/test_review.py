#!/usr/bin/python3
"""Defines unittests for models/review.py."""

import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.review import Review


class TestReview_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Review class."""

    def test_no_args_instantiates(self):
        self.assertEqual(Review, type(Review()))

    def test_new_instance_that_is_stored_in_objects(self):
        self.assertIn(Review(), models.storage.all().values())

    def test_id_is_str(self):
        self.assertEqual(str, type(Review().id))

    def test_created_at_datetime(self):
        self.assertEqual(datetime, type(Review().created_at))

    def test_updated_at_datetime(self):
        self.assertEqual(datetime, type(Review().updated_at))

    def test_place_id_is_class_attribute(self):
        rv = Review()
        self.assertEqual(str, type(Review.place_id))
        self.assertIn("place_id", dir(rv))
        self.assertNotIn("place_id", rv.__dict__)

    def test_user_id_is_class_attribute(self):
        rv = Review()
        self.assertEqual(str, type(Review.user_id))
        self.assertIn("user_id", dir(rv))
        self.assertNotIn("user_id", rv.__dict__)

    def test_unique_ids_of_two_reviews(self):
        rv1 = Review()
        rv2 = Review()
        self.assertNotEqual(rv1.id, rv2.id)

    def test_text_is_class_attribute(self):
        rv = Review()
        self.assertEqual(str, type(Review.text))
        self.assertIn("text", dir(rv))
        self.assertNotIn("text", rv.__dict__)

    def test_two_reviews_created_at_differently(self):
        rv1 = Review()
        sleep(1)
        rv2 = Review()
        self.assertLess(rv1.created_at, rv2.created_at)

    def test_two_reviews_updated_at_differently(self):
        rv1 = Review()
        sleep(1)
        rv2 = Review()
        self.assertLess(rv1.updated_at, rv2.updated_at)

    def test_unused_args(self):
        rv = Review(None)
        self.assertNotIn(None, rv.__dict__.values())

    def test_instantiation_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        rv = Review(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(rv.id, "345")
        self.assertEqual(rv.created_at, dt)
        self.assertEqual(rv.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Review(id=None, created_at=None, updated_at=None)

    def test_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        rv = Review()
        rv.id = "123456"
        rv.created_at = rv.updated_at = dt
        rvstr = rv.__str__()
        self.assertIn("[Review] (123456)", rvstr)
        self.assertIn("'id': '123456'", rvstr)
        self.assertIn("'created_at': " + dt_repr, rvstr)
        self.assertIn("'updated_at': " + dt_repr, rvstr)


class TestReview_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the Review class."""

    def test_type_of_to_dict(self):
        self.assertTrue(dict, type(Review().to_dict()))

    def test_to_dict_has_added_attributes(self):
        rv = Review()
        rv.middle_name = "Holberton"
        rv.my_number = 98
        self.assertEqual("Holberton", rv.middle_name)
        self.assertIn("my_number", rv.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        rv = Review()
        rv_dict = rv.to_dict()
        self.assertEqual(str, type(rv_dict["id"]))
        self.assertEqual(str, type(rv_dict["created_at"]))
        self.assertEqual(str, type(rv_dict["updated_at"]))

    def test_output_of_to_dict(self):
        dt = datetime.today()
        rv = Review()
        rv.id = "123456"
        rv.created_at = rv.updated_at = dt
        tdict = {
            'id': '123456',
            '__class__': 'Review',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
        }
        self.assertDictEqual(rv.to_dict(), tdict)

    def test_to_dict_has_correct_keys(self):
        rv = Review()
        self.assertIn("id", rv.to_dict())
        self.assertIn("created_at", rv.to_dict())
        self.assertIn("updated_at", rv.to_dict())
        self.assertIn("__class__", rv.to_dict())

    def test_to_dict_method_is_not_same_as_instance_dict(self):
        rv = Review()
        self.assertNotEqual(rv.to_dict(), rv.__dict__)

    def test_to_dict_with_arg(self):
        rv = Review()
        with self.assertRaises(TypeError):
            rv.to_dict(None)

    def setUp(self):
        """Sets up test methods."""
        pass

    def tearDown(self):
        """Tears down test methods."""
        pass

    def test_for_one_save(self):
        rv = Review()
        sleep(1)
        first_updated_at = rv.updated_at
        rv.save()
        self.assertLess(first_updated_at, rv.updated_at)

    def test_for_two_saves(self):
        rv = Review()
        sleep(1)
        first_updated_at = rv.updated_at
        rv.save()
        second_updated_at = rv.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(1)
        rv.save()
        self.assertLess(second_updated_at, rv.updated_at)

    def test_save_with_arg(self):
        rv = Review()
        with self.assertRaises(TypeError):
            rv.save(None)

    def test_save_updates_of_file(self):
        rv = Review()
        rv.save()
        rvid = "Review." + rv.id
        with open("hbnb.json", "r") as f:
            self.assertIn(rvid, f.read())


if __name__ == "__main__":
    unittest.main()
