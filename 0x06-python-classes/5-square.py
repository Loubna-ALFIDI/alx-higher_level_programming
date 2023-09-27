#!/usr/bin/python3
""" 1-square.py """


class Square:
    """ Square class """
    def __init__(self, __size=0):
        if type(__size) != int:
            raise TypeError("size must be an integer")
        elif __size < 0:
            raise ValueErrorError("size must be >= 0")
        else:
            self.__size = __size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, x):
        if type(x) != int:
            raise TypeError("size must be an integer")
        elif x < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = x

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            for i in range(0, self.__size):
                for j in range(0, self.__size):
                    print("#", end="")
                print()
