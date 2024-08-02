#!/usr/bin/python3
"""Python script that authenticates a github user given
username and password<PAT> as parameter
"""
import requests
import sys
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    url = 'https://api.github.com/user'
    basic = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    req = requests.get(url, auth=basic)
    print(req.json().get('id'))
