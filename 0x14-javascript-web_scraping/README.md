Star Wars Characters by Movie
This Node.js script fetches the characters for a specific Star Wars movie based on the movie ID provided as a command-line argument. The script then logs the names of the characters to the console.

Prerequisites
Node.js installed on your machine
request module installed (npm install request)
Usage
Clone the repository:

git clone https://github.com/yourusername/star-wars-characters-by-movie.git
cd star-wars-characters-by-movie
Install dependencies:

npm install
Run the script with the movie ID as a command-line argument:

node index.js &lt;movie-id>
Replace <movie-id> with the ID of the Star Wars movie you want to fetch characters for.

Example
To fetch the characters for Star Wars: Episode IV - A New Hope (movie ID: 1):

node index.js 1
The output will be a list of character names:

Characters of "A New Hope":
Luke Skywalker
C-3PO
R2-D2
Darth Vader
...
