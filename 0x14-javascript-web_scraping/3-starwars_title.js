#!/usr/bin/node

const request = require('request');
const iduser = process.argv[2];

request(`https://swapi-api.alx-tools.com/api/films/${iduser}`, { json: true }, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    console.log(body.title);
  }
});
