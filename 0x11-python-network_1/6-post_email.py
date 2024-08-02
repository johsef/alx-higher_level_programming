#!/usr/bin/python3
"""Python script that displays the response of a url when passed email
passed as parameter in a POST request
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    req = requests.post(url, data={'email': sys.argv[2]})
    print(req.text)
