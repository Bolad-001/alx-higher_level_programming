#!/usr/bin/python3
"""Unit tests for the Rectangle class"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangleClass(unittest.TestCase):
    """Tests for the Rectangle class functionality"""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_rectangle_instance_creation(self):
        """Test creating a rectangle instance and its attributes"""
        r0 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r0.id, 5)
        self.assertEqual(r0.width, 1)
        self.assertEqual(r0.height, 2)
        self.assertEqual(r0.x, 3)
        self.assertEqual(r0.y, 4)
        self.assertEqual(r0.area(), 2)

        expected_dict = {'x': 3, 'y': 4, 'id': 5, 'height': 2, 'width': 1}
        self.assertEqual(r0.to_dictionary(), expected_dict)

        # Test various update scenarios
        r0.update()
        r0.update(89)
        r0.update(89, 1)
        r0.update(89, 1, 2)
        r0.update(89, 1, 2, 3)
        r0.update(89, 1, 2, 3, 4)
        r0.update(**{'id': 89})
        r0.update(**{'id': 89, 'width': 1})
        r0.update(**{'id': 89, 'width': 1, 'height': 2})
        r0.update(**{'id': 89, 'width': 1, 'height': 2, 'x': 3})
        r0.update(**{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})

        r0_dict = r0.to_dictionary()
        r1 = Rectangle.create(**r0_dict)
        self.assertIsNot(r0, r1)

    def test_type_error_handling(self):
        """Test handling TypeError"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("1", 2)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "2")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, "3")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, "4")

    def test_value_error_handling(self):
        """Test handling ValueError"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-1, 2)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, -2)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(1, 2, -3)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(1, 2, 3, -4)


if __name__ == '__main__':
    unittest.main()
