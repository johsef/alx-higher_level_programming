#!/bin/bash
#Bash script that sends a DELETE request to the URLpassed as the first argument and displays the body of the response
curl -sX DELETE "$1"
