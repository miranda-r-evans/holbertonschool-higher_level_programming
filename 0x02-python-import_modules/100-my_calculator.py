#!/usr/bin/python3

from sys import argv
from calculator_1 import add, sub, mul, div


def main():
    pass

if __name__ == '__main__':
    if not len(argv) == 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        str = argv[1] + ' ' + argv[2] + ' ' + argv[3] + ' ='
        if argv[2] == '+':
            print(str, add(int(argv[1]), int(argv[3])))
        elif argv[2] == '-':
            print(str, sub(int(argv[1]), int(argv[3])))
        elif argv[2] == '*':
            print(str, mul(int(argv[1]), int(argv[3])))
        elif argv[2] == '/':
            print(str, div(int(argv[1]), int(argv[3])))
        else:
            print('Unknown operator. Available operators: +, -, * and /')
            exit(1)
