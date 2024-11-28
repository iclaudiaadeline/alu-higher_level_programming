#!/usr/bin/python3
"""Test for Square"""

import unittest
from models.square import Square

class TestSquare(unittest.TestCase):
    def test_square_creation(self):
        s = Square(5)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)

    def test_invalid_size(self):
        with self.assertRaises(TypeError):
            Square("5")
        with self.assertRaises(ValueError):
            Square(-5)
        with self.assertRaises(ValueError):
            Square(0)

    def test_area(self):
        s = Square(4)
        self.assertEqual(s.area(), 16)

    def test_to_dictionary(self):
        s = Square(10, 2, 1, 1)
        s_dict = s.to_dictionary()
        self.assertEqual(s_dict['size'], 10)
        self.assertEqual(s_dict['x'], 2)
        self.assertEqual(s_dict['y'], 1)

    def test_update(self):
        s = Square(5)
        s.update(10, 7, 2, 3)
        self.assertEqual(s.id, 10)
        self.assertEqual(s.size, 7)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

if __name__ == "__main__":
    unittest.main()

