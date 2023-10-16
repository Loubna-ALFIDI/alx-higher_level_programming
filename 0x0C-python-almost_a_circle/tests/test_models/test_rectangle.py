#!/usr/bin/python3
"""test module for rectangle"""
import os
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


current_path = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_path, '..'))
sys.path.insert(0, project_root)


class TestRectangle(unittest.TestCase):
    
    def test_is_inheritance(self):
        """test is inheritance"""
        self.assertTrue(issubclass(Rectangle, Base))
    
    def test_no_args(self):
        """no args test"""
        with self.assertRaises(TypeError) as e:
            r = Rectangle()
        self.assertEqual(type(e.exception), TypeError)

    def test_rec_id(self):
        """test rec id"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 4)
        r3 = Rectangle(10, 7, 2, 8, 12)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r3.id, 12)

    def test_rec_error(self):
        """test rec error"""
        with self.assertRaises(TypeError) as e:
            g = Rectangle("1", 2)
        message = "width must be an integer"
        self.assertEqual(str(e.exception), message)
        
        with self.assertRaises(TypeError) as e:
            r = Rectangle(1, "2")
        message = "height must be an integer"
        self.assertEqual(str(e.exception), message)

        with self.assertRaises(ValueError) as e:
            r = Rectangle(1, 2, -1)
        message = "x must be >= 0"
        self.assertEqual(str(e.exception), message)

        with self.assertRaises(TypeError) as e:
            r = Rectangle(1, 2, 3, "4")
        message = "y must be an integer"
        self.assertEqual(str(e.exception), message)

        with self.assertRaises(ValueError) as e:
            r = Rectangle(-1, 2)
        message = "width must be > 0"
        self.assertEqual(str(e.exception), message)

        with self.assertRaises(ValueError) as e:
            r = Rectangle(1, -2)
        message = "height must be > 0"
        self.assertEqual(str(e.exception), message)

        with self.assertRaises(ValueError) as e:
            r = Rectangle(0, 2)
        message = "width must be > 0"
        self.assertEqual(str(e.exception), message)

        with self.assertRaises(ValueError) as e:
            r = Rectangle(1, 0)
        message = "height must be > 0"
        self.assertEqual(str(e.exception), message)

        with self.assertRaises(ValueError) as e:
            r = Rectangle(1, 2, -3)
        message = "x must be >= 0"
        self.assertEqual(str(e.exception), message)

        with self.assertRaises(ValueError) as e:
            r = Rectangle(1, 2, 3, -4)
        message = "y must be >= 0"
        self.assertEqual(str(e.exception), message)

    def test_area(self):
        """test area"""
        r = Rectangle(1, 2)
        self.assertEqual(r.area(), 2)
    
    def test_str(self):
        """test str"""
        Base._Base__nb_objects = 0
        r = Rectangle(1, 2)
        self.assertEqual(str(r), "[Rectangle] (1) 0/0 - 1/2")

    def test_display(self):
        """test display"""
        Base._Base__nb_objects = 0
        r = Rectangle(4, 3)
        self.assertEqual(r.width, 4)
        self.assertEqual(r.height, 3)

    def test_more_display(self):
        """test more display"""
        Base._Base__nb_objects = 0
        r = Rectangle(2, 3, 2, 2)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 2)

    def test_update(self):
        """test update"""
        Base._Base__nb_objects = 0
        r = Rectangle(10, 10, 10, 10)
        msg = "[Rectangle] (1) 10/10 - 10/10"
        self.assertEqual(str(r), msg)
        r.update(89)
        msg1 = "[Rectangle] (89) 10/10 - 10/10"
        self.assertEqual(str(r), msg1)
        r.update(89, 2)
        msg2 = "[Rectangle] (89) 10/10 - 2/10"
        self.assertEqual(str(r), msg2)
        r.update(89, 2, 3)
        msg3 = "[Rectangle] (89) 10/10 - 2/3"
        self.assertEqual(str(r), msg3)
        r.update(89, 2, 3, 4)
        msg4 = "[Rectangle] (89) 4/10 - 2/3"
        self.assertEqual(str(r), msg4)
        r.update(89, 2, 3, 4, 5)
        msg5 = "[Rectangle] (89) 4/5 - 2/3"
        self.assertEqual(str(r), msg5)
    
    def test_more_update(self):
        """test more update"""
        Base._Base__nb_objects = 0
        r = Rectangle(10, 10, 10, 10)
        msg = "[Rectangle] (1) 10/10 - 10/10"
        self.assertEqual(str(r), msg)
        r.update(height=1)
        msg1 = "[Rectangle] (1) 10/10 - 10/1"
        self.assertEqual(str(r), msg1)
        r.update(width=1, x=2)
        msg2 = "[Rectangle] (1) 2/10 - 1/1"
        self.assertEqual(str(r), msg2)
        r.update(y=1, width=2, x=3, id=89)
        msg3 = "[Rectangle] (89) 3/1 - 2/1"
        self.assertEqual(str(r), msg3)
        r.update(x=1, height=2, y=3, width=4)
        msg4 = "[Rectangle] (89) 1/3 - 4/2"
        self.assertEqual(str(r), msg4)

        def test_to_dict(self):
            """test to dict"""
            Base._Base__nb_objects = 0
            r1 = Rectangle(10, 2, 1, 9)
            self.assertEqual(str(r1), "[Rectangle] (1) 1/9 - 10/2")
            self.assertEqual(r1.to_dictionary(), {'x': 1, 'y': 9, 'id': 1, 'width': 10, 'height': 2})
            r2 = Rectangle(1, 1)
            self.assertEqual(str(r2), "[Rectangle] (2) 0/0 - 1/1")
            self.assertEqual(r2.to_dictionary(), {'x': 0, 'y': 0, 'id': 2, 'width': 1, 'height': 1})


if __name__ == '__main__':
    unittest.main()
