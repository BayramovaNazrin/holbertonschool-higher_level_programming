#!/usr/bin/python3
# Error code
"""
takes in a URL, sends a request to the URL and displays the body of the response
"""
import urllib.request
import sys
if __name__ == '__main__':
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            body = response.read()

        print(body.decode('utf-8'))
    except urllib.error.HTTPError as Err:
        print("Error code:", Err.code)
