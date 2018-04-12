#!/usr/bin/python3

import hidden_4


array = dir(hidden_4)
for mem in array:
    if not mem.startswith('__'):
        print(mem)
