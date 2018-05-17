#!/usr/bin/python3
''' module with file appending function '''


def append_write(filename="", text=""):
    ''' function that appends text to end of file '''
    with open(filename, mode='a', encoding='utf-8') as f:
        chars_read = f.write(text)
    return chars_read
