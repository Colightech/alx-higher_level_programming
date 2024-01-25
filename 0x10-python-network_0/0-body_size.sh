#!/bin/bash

# Check if the URL is provided as an argument
if [ $# -eq 0 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

url=$1

response_size=$(curl -sI "$url" | grep -i content-length | awk '{print $2}' | tr -d '\r\n')


if [ -z "$response_size" ]; then
    echo "Content-Length header not found in the response."
else
    echo "Size of the response body: $response_size bytes"
fi
