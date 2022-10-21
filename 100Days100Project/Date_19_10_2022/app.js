$('textarea').keyup(function() {
    var textlen = $(this).val().length;
    $('.letter').text(textlen);
  });

  $('textarea').keyup(function () { 
    var word = $('textarea').val().split(' ');
    if ($('textarea').val().length == 0) {
        $('.word').text("0");        
    } else {
        $('.word').text(word.length);
    }   
  });