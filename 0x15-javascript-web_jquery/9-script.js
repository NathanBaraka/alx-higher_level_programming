// Queries the API for wind speed in SF and replaces the txt of
// div#sf_wind_speed tag with the speed

let url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
$.get(url, function (data) {
  let wind = data.query.results.channel.wind.speed;
  $('div#sf_wind_speed').text(wind);
});
