#!/bin/bash
# script request to URL/catch_me passed as the first argument,displays the body.
curl -s -X PUT 0.0.0.0:5000/catch_me -d "user_id=98" -H "Origin: HolbertonSchool" -L
