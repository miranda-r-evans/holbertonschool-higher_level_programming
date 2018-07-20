#!/usr/bin/python3
"""
script to print cities in a given state
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

        cursor.execute('''SELECT cities.name
                        FROM cities
                        INNER JOIN states
                        ON states.id=cities.state_id
                        WHERE states.name=%s;''', (sys.argv[4],))

        my_cities = cursor.fetchall()

        my_cities = ', '.join([tup[0] for tup in my_cities])

        print(my_cities)

        db.close()


if __name__ == "__main__":
        main()
