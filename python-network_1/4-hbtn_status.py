#!/usr/bin/python3
# whats my status?
"""
script that fetches url
"""
import request
if __name__ == '__main__':
    url = 'https://intranet.hbtn.io/status'

    response = requests.get(url)

    print("Body response:")
    print("\t- type: {}".format(type(reponse.text)))
    print("\t- content: {}".format(response.text))
