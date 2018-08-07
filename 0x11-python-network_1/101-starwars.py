#!/usr/bin/python3
'''
searches with swapi
'''

from requests import get
from sys import argv


if __name__ == "__main__":
        url = 'https://swapi.co/api/people/?search={}'.format(argv[1])
        response = get(url)
        results = eval(response.text.replace('null', '""'))
        print('Number of results: {}'.format(results.get('count')))
        for item in results.get('results'):
                print(item.get('name'))
        url = results.get('next')
        while url is not '':
                response = get(url)
                results = eval(response.text.replace('null', '""'))
                for item in results.get('results'):
                        print(item.get('name'))
                url = results.get('next')
