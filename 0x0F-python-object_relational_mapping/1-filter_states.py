#!/usr/bin/python3
"""
script to print states with a name beginning with 'N'
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

        cursor.execute("SELECT id, name FROM states")

        my_states = cursor.fetchall()

        for state in my_states:
                if state[1][0] == 'N':
                        print(state)

        db.close()


if __name__ == "__main__":
        main()
