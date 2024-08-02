#!/usr/bin/python3
"""Python script displays the content in a url body or returns the
Error code
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    req = requests.get(url)
    if req.status_code >= 400:
        print('Error code: ', req.status_code)
    else:
        print(req.text)
