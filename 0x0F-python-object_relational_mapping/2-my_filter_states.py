#!/usr/bin/python3
"""
script to print states with a name given from input
"""

import MySQLdb
import sys


def main():
        """
        calls db fuctions in order to select and print states
        """

        db = MySQLdb.connect("localhost", sys.argv[1],
                             sys.argv[2], sys.argv[3])

        cursor = db.cursor()

        line = "SELECT id, name FROM states WHERE BINARY name='{}'"

        cursor.execute(line.format(sys.argv[4]))

        my_states = cursor.fetchall()

        for state in my_states:
                print(state)

        db.close()


if __name__ == "__main__":
        main()
