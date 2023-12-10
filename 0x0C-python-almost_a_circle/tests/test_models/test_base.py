#!/usr/bin/python3
""" Test module for class Base """
import unittest
from models.base import Base


class TestBaseClass(unittest.TestCase):
    """ """"

    def test_id_assignment(self):

    b1 = Base()
    b2 = Base()
    b3 = Base()
    b4 = Base(12)
    b5 = Base()


    self.assertEqual(b1.id)
    self.assertEqual(b2.b1.id + 1)
    self.assertEqual(b3.id, b2.id + 1)
    self.assertNotEqual(b4.id)


