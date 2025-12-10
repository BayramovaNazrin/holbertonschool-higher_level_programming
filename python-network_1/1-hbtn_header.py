#!/usr/bin/python3
# response header value
"""
Python script that takes in a URL, sends a request to the URL and displays
"""
import urllib.request
import sys
if __name__ == '__main__':
    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        headers = request.info()

    print(headers.get("X-Request-Id"))
