#!/usr/bin/python3
'''
posts a letter to a url
'''

from requests import post
from sys import argv


if __name__ == "__main__":
        try:
                response = post('http://0.0.0.0:5000/search_user',
                                data={'q': argv[1]})
        except Exception:
                response = post('http://0.0.0.0:5000/search_user',
                                data={'q': ''})

        try:
                attributes = eval(response.text)
                if len(attributes) == 0:
                        print('No result')
                else:
                        print('[{}] {}'.format(attributes.get('id'),
                                               attributes.get('name')))
        except Exception:
                print('Not a valid JSON')
