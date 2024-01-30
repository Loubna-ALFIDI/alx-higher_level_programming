#!/usr/bin/node

const request = require('request');
const urlAPI = process.argv[2];

request(urlAPI, { json: true }, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const number = {};
    for (const task of body) {
      if (task.completed) {
        number[task.userId] = (number[task.userId] || 0) + 1;
      }
    }
    console.log(number);
  }
});
