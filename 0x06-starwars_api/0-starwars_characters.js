#!/usr/bin/node

const request = require('request');

/**
 * Fetches JSON from a URL and returns a Promise.
 * @param {string} url - The URL to fetch.
 * @returns {Promise<Object>}
 */
function fetchJSON(url) {
  return new Promise((resolve, reject) => {
    request(url, (err, res, body) => {
      if (err) reject(err);
      else resolve(JSON.parse(body));
    });
  });
}

/**
 * Fetches and prints character names of a Star Wars movie by movieId.
 * Maintains the order of characters.
 * @param {string} movieId
 */
async function fetchAndPrintCharacters(movieId) {
  try {
    const film = await fetchJSON(`https://swapi-api.alx-tools.com/api/films/${movieId}`);
    const characters = film.characters;

    for (const url of characters) {
      const character = await fetchJSON(url);
      console.log(character.name);
    }
  } catch (err) {
    console.error(err);
  }
}

// Main
const movieId = process.argv[2];
if (!movieId) {
  console.error('Usage: ./0-starwars_characters.js <Movie ID>');
  process.exit(1);
}

fetchAndPrintCharacters(movieId);
