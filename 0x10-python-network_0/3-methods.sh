#!/bin/bash
#  script that takes in a URL and displays all HTTP methods
curl -si "$1" | awk -F ": " '/Allow/ {print $2}'
