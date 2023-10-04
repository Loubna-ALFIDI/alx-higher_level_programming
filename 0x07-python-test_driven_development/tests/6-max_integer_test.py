#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Unittests for max_integer([..])"""
    def test0(self):
        """Test max_integer([..])"""
        test_0 = max_integer([1, 2, 3, 4])
        self.assertEqual(test_0, 4)

    def test1(self):
        """Test max_integer([..])"""
        test_1 = max_integer([1, 3, 4, 2])
        self.assertEqual(test_1, 4)

    def test2(self):
        """Test max_integer([..])"""
        test_2 = max_integer([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
        self.assertEqual(test_2, 9)

    def test3(self):
        """Test max_integer([..])"""
        test_3 = max_integer([])
        self.assertEqual(test_3, None)


if __name__ == '__main__':
    unittest.main()
