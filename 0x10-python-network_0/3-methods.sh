#!/bin/bash
# This shows all HTTP methods that the server will accept.
curl -s -I "${1}" | grep "^Allow: .*" | cut -d " " -f 2-
