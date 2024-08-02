#!/usr/bin/python3
"""Displays the body response of a POST request with
an email as the parameter.
"""
import sys
import urllib.request
import urllib.parse


if __name__ == "__main__":
    url = sys.argv[1]
    data = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(data)
    data = data.encode('ascii')

    request = urllib.request.Request(url, data)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
