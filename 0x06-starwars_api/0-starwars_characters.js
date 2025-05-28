#!/usr/bin/node

const request = require('request');

/**
 * Fetches and prints the names of characters in a Star Wars movie.
 * @param {string} movieId - The ID of the Star Wars movie.
 */
async function fetchMovieCharacters(movieId) {
  const url = `https://swapi-api.hbtn.io/api/films/${movieId}`;

  try {
    /**
     * Fetches the list of character URLs for a given movie ID.
     * @returns {Promise<Array>>} A promise that resolves to an array of character URLs.
     */
    const characters = await new Promise((resolve, reject) => {
      request(url, (err, res, body) => {
        if (err) {
          reject(err);
        } else {
          resolve(JSON.parse(body).characters);
        }
      });
    });

    /**
     * Iterates over character URLs, fetches each character's name, and prints it.
     */
    for (const characterUrl of characters) {
      const name = await new Promise((resolve, reject) => {
        request(characterUrl, (err, res, body) => {
          if (err) {
            reject(err);
          } else {
            resolve(JSON.parse(body).name);
          }
        });
      });
      console.log(name);
    }
  } catch (err) {
    console.error('Error:', err.message);
  }
}

/**
 * Main execution: Checks if a movie ID is provided and fetches the movie characters.
 */
const movieId = process.argv[2];
if (!movieId) {
  console.error('Usage: ./script.js <Movie ID>');
  process.exit(1);
}

fetchMovieCharacters(movieId);
