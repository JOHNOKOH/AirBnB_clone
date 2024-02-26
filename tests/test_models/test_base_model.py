#!/usr/bin/python3
"""base_model.py module"""

import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):

    def test_id_is_string(self):
        base_model = BaseModel()
        self.assertIsInstance(base_model.id, str)

    def test_unique_id(self):
        bm_1 = BaseModel()
        bm_2 = BaseModel()
        self.assertNotEqual(bm_1.id, bm_2.id)

    def test_created_at_is_datetime(self):
        base_model = BaseModel()
        self.assertIs(type(base_model.created_at), datetime)

    def test_to_dict(self):
        bm = BaseModel()
        bm.name = "My First Model"
        bm.my_number = 89
        bm_json = bm.to_dict()
        self.assertIs(type(bm_json), dict)

    def test_no_args_instantiates(self):
        self.assertEqual(type(BaseModel()), BaseModel)

    def test_created_at_is_same_as_updated_at(self):
        bm = BaseModel()
        self.assertEqual(bm.created_at, bm.updated_at)

    def test_id_not_none(self):
        base_model = BaseModel()
        self.assertIsNotNone(base_model.id)

    def test_created_at_is_not_same_as_updated_at_after_save(self):
        bm = BaseModel()
        initial_created_at = bm.created_at
        initial_updated_at = bm.updated_at
        import time
        time.sleep(1)
        bm.save()
        self.assertNotEqual(initial_created_at, bm.updated_at)
        self.assertEqual(initial_updated_at, bm.created_at)

    def test_to_dict_has_class_key(self):
        bm = BaseModel()
        base_dict = bm.to_dict()
        self.assertIn('__class__', base_dict)

    def test_to_dict_datetime_format(self):
        bm = BaseModel()
        base_dict = bm.to_dict()
        self.assertEqual(base_dict['created_at'], bm.created_at.isoformat())
        self.assertEqual(base_dict['updated_at'], bm.updated_at.isoformat())

    def test_args_unused(self):
        bm = BaseModel
        self.assertNotIn(None, bm.__dict__.values())

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

    def test_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        bm = BaseModel()
        bm.id = "123456"
        bm.created_at = bm.updated_at = dt
        bmstr = bm.__str__()
        self.assertIn("[BaseModel] (123456)", bmstr)
        self.assertIn("'id': '123456'", bmstr)
        self.assertIn("'created_at': " + dt_repr, bmstr)
        self.assertIn("'updated_at': " + dt_repr, bmstr)

    def testSave(self):
        """ Checks if save method updates the public instance instance
        attribute updated_at """
        self.my_model.first_name = "First"
        self.my_model.save()

        self.assertIsInstance(self.my_model.id, str)
        self.assertIsInstance(self.my_model.created_at, datetime.datetime)
        self.assertIsInstance(self.my_model.updated_at, datetime.datetime)

        first_dict = self.my_model.to_dict()

        self.my_model.first_name = "Second"
        self.my_model.save()
        sec_dict = self.my_model.to_dict()

        self.assertEqual(first_dict['created_at'], sec_dict['created_at'])
        self.assertNotEqual(first_dict['updated_at'], sec_dict['updated_at'])
