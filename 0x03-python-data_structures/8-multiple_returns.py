#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if sentence is False:
        return (length, None)
    else:
        return (length, sentence[0])
