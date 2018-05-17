#!/usr/bin/python3
''' module with string-insertion function '''


def append_after(filename="", search_string="", new_string=""):
    ''' after search_string appears in a line of the file,
    new_string will be inserted '''
    to_write = ''
    with open(filename, 'r') as f:
        line = f.readline()
        while line != '':
            to_write = to_write + line
            if line.count(search_string) != 0:
                to_write = to_write + new_string
            line = f.readline()

    with open(filename, 'w') as f:
        f.write(to_write)
