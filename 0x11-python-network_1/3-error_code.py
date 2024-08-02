#!/usr/bin/python3
"""Displays the Error code for a given url request if any
"""
import sys
import urllib.request
import urllib.parse


if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(request) as response:
            print(response.read().decode('utf-8'))

    except urllib.error.HTTPError as err:
        print('Error code:', err.code)
