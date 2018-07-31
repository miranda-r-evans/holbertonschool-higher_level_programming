#!/usr/bin/env bash
# displays content length
curl -sI "$1" | grep "Content-Length" | cut -d' ' -f2
