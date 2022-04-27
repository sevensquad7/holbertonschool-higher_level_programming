#!/usr/bin/python3
import urllib.request
import urllib.parse
import sys
url = sys.argv[1]
email = sys.argv[2]
values = {'email': email}
data = urllib.parse.urlencode(values)
data = data.encode('ascii')
req = urllib.request.Request(url, data)
with urllib.request.urlopen(req) as response:
    print(response.read().decode('utf-8'))
