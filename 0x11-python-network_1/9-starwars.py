#!/usr/bin/python3
'''
searches with swapi
'''

from requests import get
from sys import argv


response = get('https://swapi.co/api/people/?search={}'.format(argv[1]))

results = eval(response.text.replace('null', '""'))
print('Number of results: {}'.format(results['count']))
for item in results['results']:
        print(item['name'])
