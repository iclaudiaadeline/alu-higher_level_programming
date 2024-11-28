#!/usr/bin/env python3
"""Unit tests for Base, Rectangle, and Square classes"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import os


class TestBase(unittest.TestCase):
    """Test cases for Base class"""

    def setUp(self):
        """Reset nb_objects before each test"""
        Base._Base__nb_objects = 0

    def test_base_init(self):
        """Test Base instance initialization"""
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base(89)
        self.assertEqual(b3.id, 89)

    def test_to_json_string(self):
        """Test JSON string conversion"""
        json_str = Base.to_json_string([{'id': 1}])
        self.assertEqual(json_str, '[{"id": 1}]')
        self.assertEqual(Base.to_json_string([]), '[]')
        self.assertEqual(Base.to_json_string(None), '[]')


class TestRectangle(unittest.TestCase):
    """Test cases for Rectangle class"""

    def setUp(self):
        """Reset nb_objects before each test"""
        Base._Base__nb_objects = 0

    def test_rectangle_init(self):
        """Test Rectangle instance initialization"""
        r1 = Rectangle(10, 5)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 5)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r1.id, 1)

    def test_rectangle_validation(self):
        """Test Rectangle attribute validation"""
        with self.assertRaises(TypeError):
            Rectangle("10", 5)
        with self.assertRaises(TypeError):
            Rectangle(10, "5")
        with self.assertRaises(ValueError):
            Rectangle(-10, 5)
        with self.assertRaises(ValueError):
            Rectangle(10, -5)
        with self.assertRaises(ValueError):
            Rectangle(0, 5)
        with self.assertRaises(ValueError):
            Rectangle(10, 0)

    def test_area(self):
        """Test area calculation"""
        r1 = Rectangle(10, 5)
        self.assertEqual(r1.area(), 50)
        r2 = Rectangle(3, 2)
        self.assertEqual(r2.area(), 6)

    def test_str_representation(self):
        """Test string representation"""
        r1 = Rectangle(4, 6, 2, 1, 12)
        expected = "[Rectangle] (12) 2/1 - 4/6"
        self.assertEqual(str(r1), expected)


class TestSquare(unittest.TestCase):
    """Test cases for Square class"""

    def setUp(self):
        """Reset nb_objects before each test"""
        Base._Base__nb_objects = 0

    def test_square_init(self):
        """Test Square instance initialization"""
        s1 = Square(5)
        self.assertEqual(s1.size, 5)
        self.assertEqual(s1.width, 5)
        self.assertEqual(s1.height, 5)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)
        self.assertEqual(s1.id, 1)

    def test_square_validation(self):
        """Test Square attribute validation"""
        with self.assertRaises(TypeError):
            Square("5")
        with self.assertRaises(ValueError):
            Square(-5)
        with self.assertRaises(ValueError):
            Square(0)

    def test_square_update(self):
        """Test update method"""
        s1 = Square(5)
        s1.update(10)
        self.assertEqual(s1.id, 10)
        s1.update(1, 2)
        self.assertEqual(s1.size, 2)
        s1.update(1, 2, 3)
        self.assertEqual(s1.x, 3)
        s1.update(1, 2, 3, 4)
        self.assertEqual(s1.y, 4)

    def test_to_dictionary(self):
        """Test dictionary representation"""
        s1 = Square(10, 2, 1, 1)
        s1_dict = s1.to_dictionary()
        expected = {'id': 1, 'x': 2, 'size': 10, 'y': 1}
        self.assertEqual(s1_dict, expected)


if __name__ == '__main__':
    unittest.main()
