#!/usr/bin/python3
def safe_print_division(a, b):

    try:
        ins = a / b
    except (TypeError, ZeroDivisionError):
        ins = None
    finally:
        print("Inside result: {}".format(ins))
    return ins
