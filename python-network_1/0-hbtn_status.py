#!/usr/bin/python3
#fetch url
"""
Fetches https://alx-intranet.hbtn.io/status and prints the response.
"""
import urllib.request
with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
    html = response.read()
