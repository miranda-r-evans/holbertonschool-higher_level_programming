#!/bin/bash
# displays allowed methods
curl -sI "$1" | grep 'Allow' | cut -d':' -f2 | cut -c 2-
