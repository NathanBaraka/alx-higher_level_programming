#!/usr/bin/node

// Import the 'request' module, which provides an API for performing HTTP requests.
const request = require('request');

// Construct the URL for the specific Star Wars film.
// The URL is a combination of a base URL and a film ID specified as the second command-line argument (process.argv[2]).
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

// Use the 'request' module to perform an HTTP GET request to the constructed URL.
// The request function takes three arguments: the URL, a callback function, and an optional options object.
request(url, function (error, response, body) {
  // The callback function takes three arguments: 'error', 'response', and 'body'.
  // If an error occurs during the request, the 'error' parameter will contain an error object.
  // If the request is successful, the 'response' parameter will contain information about the HTTP response, and the 'body' parameter will contain the response body as a string.

  // If an error occurs, log the error to the console.
  // If the request is successful, parse the response body as JSON and log the 'title' property to the console.
  console.log(error || JSON.parse(body).title);
});
