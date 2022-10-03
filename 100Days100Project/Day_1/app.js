$(document).ready(function () {
    $('input').click(function () { 
        $('body').toggleClass('active');
        $("#darktheme").text(($("#darktheme").text() == 'Light') ? 'Dark' : 'Light');
    });
});