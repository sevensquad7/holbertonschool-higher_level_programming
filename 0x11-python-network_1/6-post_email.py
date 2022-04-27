#!/usr/bin/python3
import requests
from sys import argv
url = argv[1]
email = argv[2]
values = {'email': email}
request = requests.post(url, data=values)
print(request.text)
