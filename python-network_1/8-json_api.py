#!/usr/bin/python3
# search API
"""
takes in a letter and sends a POST request to url with parameter
"""
import sys
import requests
if __name__ == '__main__':
    q = sys.argv[1] if len(sys.argv) > 1 else ""
    url = 'http://0.0.0.0:5000/search_user'
    data = {"q": q}
    response = requests.post(url, data=data)

    try:
        json_data = response.json()
    except ValueError:
        print("Not a valid JSON")
        sys.exit(0)
    if not json_data:
        print("No result")
    else:
        print("[{}] {}".format(json_data.get("id"), json_data.get("name")))
