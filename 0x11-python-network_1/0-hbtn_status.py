#!/usr/bin/python3
import urllib.request
"""Python script that fetches 'https://alx-intranet.hbtn.io/status'"""


if __name__ == "__main__":
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
        r = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(r)))
        print("\t- content: {}".format(r))
        print("\t- utf8 content: {}".format(r.decode("UTF-8")))
