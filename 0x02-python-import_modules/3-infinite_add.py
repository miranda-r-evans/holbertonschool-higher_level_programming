#!/usr/bin/python3

import sys


sum = 0
bool = 0
for ar in argv:
    if bool == 1:
        sum = sum + int(ar)
    bool = 1

print(sum)
