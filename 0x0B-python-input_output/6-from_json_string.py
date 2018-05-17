#!/usr/bin/python3
''' module with json interpreting function '''

import json


def from_json_string(my_str):
    ''' returns object represented my json string '''
    return json.loads(my_str)
