// Using the jQuery API to add a red class to the header tag and turn it,
// red when the div#red_header tag is on click.

$('div#red_header').click(function () {
    $('header').addClass('red');
  });
