#!/bin/bash
# This is sending a DELETE request to the URL that is passed as the 1st arg and displays the body of the response.
curl -s -X DELETE "${1}"
