#!/usr/bin/python3
"""Unit tests for the Square class"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquareClass(unittest.TestCase):
    """Tests for the Square class functionality"""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_square_instance_creation(self):
        """Test creating a square instance and its attributes"""
        s0 = Square(1, 2, 3, 4)
        self.assertEqual(s0.id, 4)
        self.assertEqual(s0.width, 1)
        self.assertEqual(s0.height, 1)
        self.assertEqual(s0.x, 2)
        self.assertEqual(s0.y, 3)
        self.assertEqual(s0.__str__(), "[Square] (4) 2/3 - 1")
        self.assertEqual(s0.area(), 1)

        expected_dict = {'id': 4, 'x': 2, 'size': 1, 'y': 3}
        self.assertEqual(s0.to_dictionary(), expected_dict)

        # Test various update scenarios
        s0.update()
        s0.update(89)
        s0.update(89, 1)
        s0.update(89, 1, 2)
        s0.update(89, 1, 2, 3)
        s0.update(**{'id': 89})
        s0.update(**{'id': 89, 'size': 1})
        s0.update(**{'id': 89, 'size': 1, 'x': 2})
        s0.update(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})

        s0_dict = s0.to_dictionary()
        s1 = Rectangle.create(**s0_dict)
        self.assertIsNot(s0, s1)

    def test_type_error_handling(self):
        """Test handling TypeError"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("1")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, "2")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, "3")

    def test_value_error_handling(self):
        """Test handling ValueError"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-1)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(1, -2)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(1, 2, -3)


if __name__ == '__main__':
    unittest.main()
