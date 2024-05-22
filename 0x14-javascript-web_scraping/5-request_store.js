#!/usr/bin/node

// Import the built-in Node.js 'fs' module, which provides an API for interacting with the file system.
const fs = require('fs');

// Import the 'request' module, which provides an API for performing HTTP requests.
const request = require('request');

// Use the 'request' module to perform an HTTP GET request to the URL specified as the second command-line argument (process.argv[2]).
// Use the 'pipe()' method to write the response data to a file specified as the third command-line argument (process.argv[3]).
request(process.argv[2]).pipe(fs.createWriteStream(process.argv[3]));
