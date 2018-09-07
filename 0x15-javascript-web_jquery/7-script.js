$.getJSON('https://swapi.co/api/people/5/?format=json', function (result) {
  $('#character').text(result.name);
});
