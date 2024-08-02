#!/bin/bash
#Bash script that sends request to a URL and displays the size of the body
curl -s "$1" | wc -c
