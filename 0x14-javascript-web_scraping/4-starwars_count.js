#!/usr/bin/node

const request = require('request');

request('http://swapi.co/api/films/.json', function (err, response, body) {
  if (err) {
    console.log(err);
    return;
  }
  let total = 0;
  let resBody = JSON.parse(body).results;
  for (let i in resBody) {
    let characters = resBody[i]['characters'];
    for (let j in characters) {
      if (characters[j].search('18') !== -1) {
        total++;
        break;
      }
    }
  }
  console.log(total);
});
