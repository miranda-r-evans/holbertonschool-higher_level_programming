#!/usr/bin/python3
''' module with json writing function '''

import json


def save_to_json_file(my_obj, filename):
    ''' function that writes the json of an object to a file '''
    with open(filename, 'w+') as f:
        json.dump(my_obj, f)
