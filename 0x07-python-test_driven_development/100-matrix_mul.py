#!/usr/bin/python3
"""matrix_mul module"""


def matrix_mul(m_a, m_b):
    """Return the matrix multiplication of two matrices.
    Args:
        m_a (list): The first matrix.
        m_b (list): The second matrix.
    Raises:
        TypeError: If m_a or m_b is not a list.
        TypeError: If m_a or m_b is not a list of lists.
        TypeError: If m_a or m_b is not all integers or floats.
        TypeError: If m_a or m_b is not all the same size.
        ValueError: If m_a or m_b is not all the same size.
    Return:
        A new matrix
    """
    if m_a == [] or m_a == [[]]:
        raise TypeError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise TypeError("m_a can't be empty")
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
