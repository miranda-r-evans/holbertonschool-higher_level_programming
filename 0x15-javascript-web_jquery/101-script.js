$(document).ready(function () {
  $('#add_item').click(function () {
    let item = $('<li></li>').text('Item');
    $('UL.my_list').append(item);
  });
  $('#remove_item').click(function () {
    $('UL.my_list').children().last().remove();
  });
  $('#clear_list').click(function () {
    $('UL.my_list').children().remove();
  });
});
