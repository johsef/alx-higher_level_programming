#!/usr/bin/python3
"""Python script that takes in a parameter and sends a POST requests
to http://0.0.0.0:500/search_user and returns formatted body response
"""
import requests
import sys


if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) == 2:
        data = sys.argv[1];
    else:
        data = ""
    req = requests.post(url, data={'q': data})
    try:
        re = req.json()
        if re == {}:
            print("No result")
        else:
            print("[{}] {}".format(re['id'], re['name']))
    except ValueError:
        print("Not a valid JSON")
