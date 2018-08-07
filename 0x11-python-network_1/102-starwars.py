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
                for film in item.get('films'):
                                f_res = get(film)
                                f_res = eval(f_res.text.replace('null', '""'))
                                print('\t{}'.format(f_res.get('title')))
        url = results.get('next')
        while url is not '':
                response = get(url)
                results = eval(response.text.replace('null', '""'))
                for item in results.get('results'):
                        print(item.get('name'))
                        for film in item.get('films'):
                                f_res = get(film)
                                f_res = eval(f_res.text.replace('null', '""'))
                                print('\t{}'.format(f_res.get('title')))

                url = results.get('next')
