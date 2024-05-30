// Adding an LI element to the list when the div#add_item tag is on click,
// The new element must be <li>Item</li> and must be added to the UL.my_list.

$('div#add_item').click(function () {
    let element = '<li>Item</li>';
    $('ul.my_list').append(element);
  });
