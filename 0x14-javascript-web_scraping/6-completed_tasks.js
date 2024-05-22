#!/usr/bin/node

// Import the 'request' module, which provides an API for performing HTTP requests.
const request = require('request');

// Get the API URL from the second command-line argument.
const apiUrl = process.argv[2];

// Use the 'request' module to perform an HTTP GET request to the API URL.
request(apiUrl, function (error, response, body) {
  // Check if there was no error during the HTTP request and the response status code is 200 (OK).
  if (!error && response.statusCode === 200) {
    try {
      // Parse the JSON data from the response body.
      const todos = JSON.parse(body);

      // Initialize an empty object to store the count of completed todos for each user ID.
      const completed = {};

      // Iterate through each todo in the 'todos' array.
      todos.forEach((todo) => {
        // If the todo is completed, increment the count for the corresponding user ID.
        if (todo.completed) {
          // If the user ID doesn't exist in the 'completed' object, initialize it with a count of 1.
          if (completed[todo.userId] === undefined) {
            completed[todo.userId] = 1;
          // Otherwise, increment the count for the existing user ID.
          } else {
            completed[todo.userId]++;
          }
        }
      });

      // Convert the 'completed' object to a string in a specific format.
      const output = `{${Object.entries(completed).map(([key, value]) => ` '${key}': ${value}`).join(',\n ')} }`;

      // Log the output to the console if the number of user IDs in the 'completed' object is greater than 2.
      // Otherwise, log the 'completed' object itself.
      console.log(Object.keys(completed).length > 2 ? output : completed);
    } catch (parseError) {
      // Log an error message if there was an error parsing the JSON data.
      console.error('Error parsing JSON:', parseError);
    }
  } else {
    // Log an error message if there was an error during the HTTP request or the response status code is not 200 (OK).
    console.error('Error:', error);
  }
});
