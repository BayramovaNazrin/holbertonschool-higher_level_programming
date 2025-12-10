#!/usr/bin/python3
# post an email
"""
sends a POST request to the passed URL with the email as a parameter
"""
import sys
import urllib.request
import urllib.parse
if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]

    with urllib.request.urlopen(url) as response:
        body = response.read()

    print("{}".format(body.decode("utf-8")))
