#!/usr/bin/python3
"""
script to print states in a database
"""

import MySQLdb
import sys


if __name__ == "__main__":
        db = MySQLdb.connect(user=sys.argv[1],
                             passwd=sys.argv[2], db=sys.argv[3])

        cursor = db.cursor()

        cursor.execute("SELECT * FROM states")

        my_states = cursor.fetchall()

        for state in my_states:
                print(state)

        cursor.close()

        db.close()
