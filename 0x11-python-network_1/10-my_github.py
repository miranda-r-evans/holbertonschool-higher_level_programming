#!/usr/bin/python3
'''
finds github id
'''

from requests import get
from sys import argv


if __name__ == "__main__":
        url = 'https://{}:{}@api.github.com/users/{}'.format(argv[1],
                                                             argv[2],
                                                             argv[1])
        try:
                response = get(url)
                text = response.text
                text = text.replace('false',
                                    'False').replace('true',
                                                     'True').replace('null',
                                                                     '""')
                info = eval(text)
                print(info["id"])
        except Exception:
                print('None')
