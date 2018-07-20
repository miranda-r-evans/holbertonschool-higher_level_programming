#!/usr/bin/python3
"""
script to print cities
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

        cursor.execute('''SELECT cities.id, cities.name, states.name
                        FROM cities
                        INNER JOIN states
                        ON states.id=cities.state_id;''')

        my_cities = cursor.fetchall()

        for city in my_cities:
                print(city)

        db.close()


if __name__ == "__main__":
        main()
