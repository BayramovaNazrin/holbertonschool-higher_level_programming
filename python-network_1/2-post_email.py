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

    data = urllib.parse.urlencode({"email": email}).encode('ascii')
    req = urllib.request.Request(url, data=data, method='POST')

    with urllib.request.urlopen(req) as response:
        body = response.read()

    print(body.decode("utf-8"))
