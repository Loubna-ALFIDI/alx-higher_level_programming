#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    double = lambda n: n * number
    return list(map(double, my_list))
