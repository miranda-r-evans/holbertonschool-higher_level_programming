#!/usr/bin/python3

import sys


def main():
    pass

if __name__ == '__main__':
    print("{:d} arguments:".format(len(sys.argv) - 1))
    i = 0
    for ar in sys.argv:
        if i != 0:
            print("{:d}: {:s}".format(i, ar))
        i = i + 1
