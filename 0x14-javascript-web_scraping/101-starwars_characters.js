#!/usr/bin/node

const request = require('request');
const syncRequest = require('sync-request');

request('http://swapi.co/api/films/' + process.argv[2] + '/.json', function (error, response, body) {
  if (error) {
    console.log(error);
    return;
  }
  let characters = JSON.parse(body)['characters'];
  for (let i in characters) {
    let res = syncRequest('GET', characters[i]);
    console.log(JSON.parse(res.body)['name']);
  }
});
