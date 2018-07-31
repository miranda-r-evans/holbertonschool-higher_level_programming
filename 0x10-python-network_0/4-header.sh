#!/bin/bash
# sends a get request with a header parameter
curl -sX GET -H "X-HolbertonSchool-User-Id: 98" "$1"
