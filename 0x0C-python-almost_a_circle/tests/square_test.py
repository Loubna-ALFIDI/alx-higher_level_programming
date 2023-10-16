#!/usr/bin/python3
"""test module for base"""
import os
import sys


current_path = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_path, '..'))
sys.path.insert(0, project_root)
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class testSquare(unittest.TestCase):
    def test_is_inheritance(self):
        """test is inheritance"""
        self.assertTrue(issubclass(Square, Base))

    def test_no_args(self):
        """no args test"""
        with self.assertRaises(TypeError) as e:
            s = Square()
        self.assertEqual(type(e.exception), TypeError)

    def test_square_error(self):
        """test square error"""
        with self.assertRaises(TypeError) as e:
            s = Square("1")
        message = "width must be an integer"
        self.assertEqual(str(e.exception), message)

        with self.assertRaises(TypeError) as e:
            r = Square(1, "2")
        message = "x must be an integer"
        self.assertEqual(str(e.exception), message)

        with self.assertRaises(TypeError) as e:
            r = Square(1, 2, "3")
        message = "y must be an integer"
        self.assertEqual(str(e.exception), message)

        with self.assertRaises(ValueError) as e:
            r = Square(-1)
        message = "width must be > 0"
        self.assertEqual(str(e.exception), message)

        with self.assertRaises(ValueError) as e:
            r = Square(1, -2)
        message = "x must be >= 0"
        self.assertEqual(str(e.exception), message)

        with self.assertRaises(ValueError) as e:
            r = Square(1, 2, -3)
        message = "y must be >= 0"
        self.assertEqual(str(e.exception), message)

        with self.assertRaises(ValueError) as e:
            r = Square(0)
        message = "width must be > 0"
        self.assertEqual(str(e.exception), message)

    def test_str(self):
        """test str"""
        Base._Base__nb_objects = 0
        s = Square(1, 2)
        self.assertEqual(str(s), "[Square] (1) 2/0 - 1")

    def test_square(self):
        """test square"""
        Base._Base__nb_objects = 0
        s = Square(5)
        self.assertEqual(str(s), "[Square] (1) 0/0 - 5")
        s = s.area()
        self.assertEqual(s, 25)
        s1 = Square(2, 2)
        self.assertEqual(str(s1), "[Square] (2) 2/0 - 2")
        s1 = s1.area()
        self.assertEqual(s1, 4)
        s2 = Square(3, 1, 3)
        self.assertEqual(str(s2), "[Square] (3) 1/3 - 3")
        s2 = s2.area()
        self.assertEqual(s2, 9)

    def test_size(self):
        """test size"""
        Base._Base__nb_objects = 0
        s = Square(5)
        self.assertEqual(s.size, 5)
        with self.assertRaises(TypeError) as e:
            s.size = "9"
        self.assertEqual(str(e.exception), "width must be an integer")

    def test_update_Square(self):
        """test update Square"""
        Base._Base__nb_objects = 0
        s = Square(5)
        self.assertEqual(str(s), "[Square] (1) 0/0 - 5")
        s.update(10)
        self.assertEqual(str(s), "[Square] (10) 0/0 - 5")
        s.update(1, 2)
        self.assertEqual(str(s), "[Square] (1) 0/0 - 2")
        s.update(1, 2, 3)
        self.assertEqual(str(s), "[Square] (1) 0/0 - 2")
        s.update(1, 2, 3, 4)
        self.assertEqual(str(s), "[Square] (1) 4/0 - 2")

if __name__ == '__main__':
    unittest.main()
