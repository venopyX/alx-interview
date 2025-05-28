# 0x06. Star Wars API

A project to fetch and display Star Wars characters based on movie ID using the Star Wars API.

## Project Duration

- **Start**: May 26, 2025
- **End**: May 30, 2025

## Concepts

- HTTP Requests in JavaScript
- Working with RESTful APIs
- Asynchronous Programming
- Command Line Arguments in Node.js
- Array Manipulation

## Requirements

- Node.js (version 10.14.x)
- Ubuntu 20.04 LTS
- Semistandard code style
- No use of `var`

## Setup

Install Node 10 and necessary modules:

```bash
curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
sudo apt-get install -y nodejs
sudo npm install semistandard request --global
export NODE_PATH=/usr/lib/node_modules
```

## Task

### 0. Star Wars Characters

Write a script to print all characters of a Star Wars movie:

- Use the Movie ID as the first argument.
- Display character names in the order of the `/films/` endpoint.
- Utilize the Star Wars API and the `request` module.

Example:

```bash
./0-starwars_characters.js 3
```

## Repository

- **GitHub**: [alx-interview/0x06-starwars_api](https://github.com/venopyx/alx-interview)
- **File**: `0-starwars_characters.js`

## Author

- [Gemechis Chala](https://github.com/venopyx)
