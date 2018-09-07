$.getJSON('https://swapi.co/api/films/?format=json', function (result) {
  for (let element of result.results) {
    let item = $('<li></li>').text(element.title);
    $('#list_movies').append(item);
  }
});
