$(function () {
  $('#add_item').click(function () {
    let item = $('<li></li>').text('Item');
    $('UL.my_list').append(item);
  });
});
