#!/usr/bin/python3
''' module containing read_file func '''


def read_file(filename=""):
    ''' reads a file '''
    with open(filename, mode='r', encoding='utf-8') as f:
        print(f.read(), end='')
