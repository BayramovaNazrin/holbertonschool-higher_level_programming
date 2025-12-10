#!/usr/bin/python3
# whats my status?
"""
script that fetches url
"""
import sys
import urllib.request
if __name__ == '__main__':
    url = 'https://intranet.hbtn.io/status'

    with urlopen.request.openurl(url) as request:
        body = request.open()

    print("Body response: {}".format(body))
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
