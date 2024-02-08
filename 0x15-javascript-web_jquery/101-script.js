#!/usr/bin/node
$(document).ready(function () {
    $('DIV#add_item').click(function () {
      $('ul.my_list').append('<li>Item</li>');
    });
    $('DIV#remove_item').click(function () {
      $('li:last-child').remove();
    });
    $('DIV#clear_list').click(function () {
      $('ul.my_list').empty();
    });
  });
