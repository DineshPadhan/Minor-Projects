let input = $('.inner #email');
let sumbit = $('.sumbit');
let cancel = $('.fa-x');

let alartinput= () =>{ 
    // console.log(input.val());

    if (input.val() ==="") {
        $('.alert').css("display", "block");
        $('.alert').css("background", "#d9534f");
        $('.message').text("Enter The valid email address");
    } else {
        $('.alert').css("display", "block");
        $('.alert').css("background", "#67b467");
        $('.message').text(input.val()+" you are Subscribed now!"); 
    }     
};
$(cancel).click(function (e) { 
    e.preventDefault();
    $('.alert').css("display", "none");
    location.reload();
});