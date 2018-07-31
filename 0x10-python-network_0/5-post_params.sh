#!/bin/bash
# sends a post request with a header parameter
curl -sX POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD" "$1"
