#!/usr/bin/python3
''' module containing file printing func '''


def read_lines(filename="", nb_lines=0):
    ''' function that reads nb_lines of a file '''
    with open(filename, mode='r', encoding='utf-8') as f:
        if nb_lines <= 0:
            print(f.read(), end='')
        else:
            for i in range(nb_lines):
                print(f.readline(), end='')
