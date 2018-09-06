#!/usr/bin/node

const request = require('request');

request('http://swapi.co/api/films/' + process.argv[2] + '/.json', function (error, response, body) {
  if (error) {
    console.log(error);
    return;
  }
  let characters = JSON.parse(body)['characters'];
  for (let i in characters) {
    request(characters[i], function (err, res, bod) {
      if (err) {
        console.log(err);
        return;
      }
      console.log(JSON.parse(bod)['name']);
    });
  }
});
