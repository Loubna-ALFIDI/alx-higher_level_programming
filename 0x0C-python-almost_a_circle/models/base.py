#!/usr/bin/python3
"""base module"""


import json
import turtle


class Base:
    """ Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """__init__"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """to_json_string"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save_to_file"""
        filename = cls.__name__ + ".json"
        with open(filename, "w") as file:
            if list_objs is None:
                file.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                file.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """from_json_string"""
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """create"""
        if cls.__name__ == "Rectangle":
            dummy = cls(10, 10)
        if cls.__name__ == "Square":
            dummy = cls(10)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """load_from_file"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                list_dicts = Base.from_json_string(file.read())
                return [cls.create(**d) for d in list_dicts]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """save_to_file_csv"""
        filename = cls.__name__ + ".csv"
        with open(filename, "w") as file:
            if list_objs is None:
                file.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    list_dicts = [obj.to_dictionary() for obj in list_objs]
                else:
                    list_dicts = [obj.to_dictionary() for obj in list_objs]
                file.write(Base.to_json_string(list_dicts))

    @classmethod
    def load_from_file_csv(cls):
        """load_from_file_csv"""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r") as file:
                list_dicts = Base.from_json_string(file.read())
                return [cls.create(**d) for d in list_dicts]
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """ draw """
        myturtle = turtle.Turtle()
        myturtle.screen.bgcolor("#641E16")
        myturtle.pensize(3)
        myturtle.shape("turtle")

        myturtle.color("0019EA")
        for rectangle in list_rectangles:
            myturtle.showturtle()
            myturtle.penup()
            myturtle.goto(rectangle.x, rectangle.y)
            myturtle.pendown()
            for i in range(2):
                myturtle.forward(rectangle.width)
                myturtle.left(90)
                myturtle.forward(rectangle.height)
                myturtle.left(90)
            myturtle.hideturtle()

        myturtle.color("EA0019")
        for square in list_squares:
            myturtle.showturtle()
            myturtle.penup()
            myturtle.goto(square.x, square.y)
            myturtle.pendown()
            for i in range(2):
                myturtle.forward(square.width)
                myturtle.left(90)
                myturtle.forward(square.height)
                myturtle.left(90)
            myturtle.hideturtle()

        myturtle.done()
