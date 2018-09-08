$(document).ready(function () {
  $('#btn_search').click(function () {
    let input = $('#city_search').val();
    let name = input.replace(' ', '%20');
    $.getJSON('https://query.yahooapis.com/v1/public/yql?q=select%20wind%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22' + name + '%2C%20CA%22)&format=json', function (result) {
      $('#wind_speed').text(result.query.results.channel.wind.speed);
    });
  });
});
