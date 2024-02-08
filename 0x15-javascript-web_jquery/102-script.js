#!/usr/bin/node
$(document).ready(function () {
    const lang = $('INPUT#language_code').val();
    $.get('https://hellosalut.stefanbohacek.dev/?lang=' + lang, function (data) {
      $('INPUT#btn_translate').click(function () {
        $('DIV#hello').text(data.hello);
      });
    });
  });
