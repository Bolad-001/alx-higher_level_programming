#!/bin/usr/python3
"""
    function that print a text with two lines
"""


def text_indentation(text):
    """Prints a text with 2 new lines after each
        of these characters: ., ? and :
    Args:
        text : Text to check

    Return:
        New text after two lines
    """
    if type(text) != str:
        raise TypeError("text must be a string")

    punct = ['.', '?', ':']
    new_text = ""
    line = ""

    for char in text:
        line += char
        if char in punct:
            new_text += line.strip() + '\n\n'
            line = ""
    if line:
        new_text += line.strip()

    print(new_text)
