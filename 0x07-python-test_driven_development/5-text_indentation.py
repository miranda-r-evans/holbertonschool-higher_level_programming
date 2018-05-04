#!/usr/bin/python3


def text_indentation(text):
    if type(text) != str:
        raise TypeError('text must be a string')
    newline = True
    for char in text:
        if newline is True:
            if char == ' ':
                pass
            else:
                newline = False
        if newline is False:
            print(char, end='')
        if char == '.' or char == '?' or char == ':':
            print('\n')
            newline = True
    print('\n')
