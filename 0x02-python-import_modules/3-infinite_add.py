#!/usr/bin/python3

from sys import argv


def main():
    pass

if __name__ == '__main__':
    sum = 0
    bool = 0
    for ar in argv:
        if bool == 1:
            sum = sum + int(ar)
        bool = 1

    print(sum)
