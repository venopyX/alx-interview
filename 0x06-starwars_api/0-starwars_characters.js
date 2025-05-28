#!/usr/bin/node

const request = require('request');

/**
 * Fetches and prints the names of characters in a Star Wars movie in the same order as the characters list.
 * @param {string} movieId - The ID of the Star Wars movie.
 */
function fetchMovieCharacters(movieId) {
  const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

  request(url, function (err, res, body) {
    if (err) {
      console.error('Error:', err);
      return;
    }

    const actors = JSON.parse(body).characters;
    printCharactersInOrder(actors, 0);
  });
}

/**
 * Recursively prints character names in the order of the provided URLs.
 * @param {Array} actors - Array of character URLs.
 * @param {number} index - Current index in the actors array.
 */
function printCharactersInOrder(actors, index) {
  if (index === actors.length) return;

  request(actors[index], function (err, res, body) {
    if (err) {
      console.error('Error:', err);
      return;
    }

    console.log(JSON.parse(body).name);
    printCharactersInOrder(actors, index + 1);
  });
}

// Check if a movie ID is provided
const movieId = process.argv[2];
if (!movieId) {
  console.error('Usage: ./0-starwars_characters.js <Movie ID>');
  process.exit(1);
}

fetchMovieCharacters(movieId);
