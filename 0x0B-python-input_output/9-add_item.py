#!/usr/bin/python3
''' module with object-appending function '''

import json
import sys

load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file


def main(argv):
    ''' adds items to list in json file '''
    try:
        my_obj = load_from_json_file('add_item.json')
    except:
        my_obj = []

    if type(my_obj) is not list:
        my_obj = []
    for item in argv[1:]:
        my_obj.append(item)
    save_to_json_file(my_obj, 'add_item.json')

main(sys.argv)
