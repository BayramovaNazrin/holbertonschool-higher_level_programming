#!/usr/bin/python3
# github
"""
GitHub credentials (username and password) and uses the GitHub API to display id
"""
import sys
import requests
if __name__ == '__main__':
    username = sys.argv[1]
    token = sys.argv[2]
    url = 'https://api.github.com/user'
    response = requests.get(url, auth=(username, token))
    try:
        data = response.json()
    except ValueError:
        print("None")
        sys.exit(0)
    print(data.get("id"))
