#!/usr/bin/node

const request = require('request');
const iduser = process.argv[2];

request(`https://swapi-api.alx-tools.com/api/films/${iduser}`, { json: true }, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    for (const character of body.characters) {
      request(character, { json: true }, (error, response, body) => {
        if (error) {
          console.error(error);
        } else {
          console.log(body.name);
        }
      });
    }
  }
});
