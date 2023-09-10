#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence is None:
        return None
    length = len(sentence)
    first = sentence[0]
    return (length, first)
