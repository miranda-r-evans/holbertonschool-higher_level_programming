#!/usr/bin/python3
'''
fetches a webpage
'''

from requests import get


response = get('https://intranet.hbtn.io/status')
print('\t - type:', response.reason.__class__)
print('\t - content:', response.reason)
