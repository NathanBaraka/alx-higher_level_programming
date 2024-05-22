#!/usr/bin/node

// Import the 'request' module, which provides an API for performing HTTP requests.
const request = require('request');

// Get the movie ID from the second command-line argument.
const movieId = process.argv[2];

// Construct the API URL for the specific Star Wars movie.
const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

// Use the 'request' module to perform an HTTP GET request to the API URL.
request(apiUrl, function (error, response, body) {
  // Check if there was no error during the HTTP request and the response status code is 200 (OK).
  if (!error && response.statusCode === 200) {
    // Parse the JSON data from the response body.
    const movieData = JSON.parse(body);

    // Log the title of the movie.
    console.log(`Characters of "${movieData.title}":`);

    // Iterate through each character URL in the 'characters' array of the movie data.
    movieData.characters.forEach((characterUrl) => {
      // Use the 'request' module to perform an HTTP GET request to the character URL.
      request(characterUrl, function (charError, charResponse, charBody) {
        // Check if there was no error during the HTTP request and the response status code is 200 (OK).
        if (!charError && charResponse.statusCode === 200) {
          // Parse the JSON data from the response body.
          const characterData = JSON.parse(charBody);

          // Log the name of the character.
          console.log(characterData.name);
        } else {
          // Log an error message if there was an error fetching the character data.
          console.error('Error fetching character data:', charError);
        }
      });
    });
  } else {
    // Log an error message if there was an error fetching the movie data.
    console.error('Error fetching movie data:', error);
  }
});
