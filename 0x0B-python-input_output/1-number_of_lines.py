#!/usr/bin/python3
''' module containing line coounting func '''


def number_of_lines(filename=""):
    ''' returns the line count of a file '''
    i = 0
    with open(filename, mode='r', encoding='utf-8') as f:
        while f.readline() is not '':
            i = i + 1
    return (i)
