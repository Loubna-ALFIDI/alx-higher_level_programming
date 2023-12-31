#!/usr/bin/python3
""" 1-square.py """


class Square:
    """ Square class """
    def __init__(self, size=0, position=(0, 0)):
        """ initialisation new square


        Args:
            size (int): size of square
            position (int, int): The position of the new square.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) != int or type(value[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
            return
        [print() for i in range(0, self.__position[1])]
        for i in range(self.__size):
            print(" " * self.__position[0], end="")
            for j in range(0, self.__size):
                print("#", end="")
            print()

    def __str__(self) -> str:
        if self.__size != 0:
            for _ in range(self.__position[1]):
                print("")
        for i in range(self.__size):
            for _ in range(self.__position[0]):
                print(" ", end="")
            for _ in range(self.__size):
                print("#", end="")
            if i != self.__size - 1:
                print("")
        return ""
