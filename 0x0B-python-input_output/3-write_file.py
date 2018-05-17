#!/usr/bin/python3
''' module containing file writing function '''


def write_file(filename="", text=""):
    ''' writes text to a file '''
    with open(filename, mode='w', encoding='utf-8') as f:
        chars_read = f.write(text)
    return chars_read
