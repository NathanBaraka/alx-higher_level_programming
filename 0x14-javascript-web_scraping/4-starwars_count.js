#!/usr/bin/node

// Import the 'request' module, which provides an API for performing HTTP requests.
const request = require('request');

// Use the 'request' module to perform an HTTP GET request to the URL specified as the second command-line argument (process.argv[2]).
request(process.argv[2], function (error, response, body) {
  // Check if there was no error during the HTTP request.
  if (!error) {
    // Parse the JSON data and extract the "results" array.
    const results = JSON.parse(body).results;
    // Use the 'reduce()' method to iterate through the movies in the 'results' array.
    // The 'reduce()' method starts with an initial value of 0 ('0' at the end).
    console.log(results.reduce((count, movie) => {
      // Check if there is a character with ID 18 ('/18/') in the 'characters' array.
      // The 'find()' method returns the first element that satisfies the provided testing function.
      return movie.characters.find((character) => character.endsWith('/18/'))
        // If a character with ID 18 is found, increment the count by 1.
        ? count + 1
        // Otherwise, keep the count unchanged.
        : count;
    }, 0));
  }
});
