#!/usr/bin/node

const request = require('request');
// Import the 'request' module, which provides an API for performing HTTP requests.

request.get(process.argv[2])
// Use the 'request' module to perform an HTTP GET request to the URL specified as the second command-line argument (process.argv[2]).

  .on('response', function (response) {
    // Set up an event listener for the 'response' event emitted by the HTTP request.
    // The event listener is a function that takes a single argument, the 'response' object, which contains information about the HTTP response.

    console.log(`code: ${response.statusCode}`);
    // Log the HTTP status code of the response to the console.
    // The 'response.statusCode' property contains the HTTP status code of the response.
  });
