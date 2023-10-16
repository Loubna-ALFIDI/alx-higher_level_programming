#!/usr/bin/python3
""" square module """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class """
    def __init__(self, size, x=0, y=0, id=None):
        """__init__"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ size getter """
        return self.width

    @size.setter
    def size(self, value):
        """ size setter """
        self.width = value
        self.height = value

    def __str__(self):
        """str"""
        return "[Square] ({}) {}/{} - {}" \
            .format(self.id, self.x, self.y, self.size)

    def update(self, *args, **kwargs):
        """update"""
        if args and len(args) != 0:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                if i == 1:
                    self.size = arg
                if i == 2:
                    self.x = arg
                if i == 3:
                    self.y = arg
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """to_dictionary"""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
