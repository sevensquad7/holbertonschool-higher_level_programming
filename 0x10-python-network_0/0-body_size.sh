#!/bin/bash
# Write a Bash script that takes The size must be displayed in bytes
sudo curl 0.0.0.0:5000 -i -s | grep Content-Length | cut -d ' ' -f2
