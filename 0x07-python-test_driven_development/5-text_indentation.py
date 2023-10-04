#!/usr/bin/python3
"""Defines a text_indentation function."""


def text_indentation(text):
    """Prints a text with 2 new lines after each
    of these characters: ., ? and :
    Args:
        text (str): text to print
    Raises:
        TypeError: if text is not a string
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    alpha = 0
    while alpha < len(text) and text[alpha] == ' ':
        alpha += 1
    while alpha < len(text):
        print(text[alpha], end="")
        if text[alpha] == '\n' or text[alpha] == '?' or \
                text[alpha] == '.' or text[alpha] == ':':
            print('\n')
            alpha += 1
            while alpha < len(text) and text[alpha] == " ":
                alpha += 1
            continue
        alpha += 1
