#!/usr/bin/node

const request = require('request');
const iduser = process.argv[2];
const util = require('util');

const prequest = util.promisify(request);

(async () => {
  try {
    const body = (await prequest(`https://swapi-api.alx-tools.com/api/films/${iduser}`, { json: true })).body;
    for (const character of body.characters) {
      const body = (await prequest(character, { json: true })).body;
      console.log(body.name);
    }
  } catch (error) {
    console.error(error);
  }
})();
