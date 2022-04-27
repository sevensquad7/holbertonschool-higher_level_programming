#!/usr/bin/python3
import urllib.request
from urllib.error import HTTPError
import sys
try:
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        print(response.read().decode('utf-8'))
except HTTPError as error:
    print("Error code: {}".format(error.code))
