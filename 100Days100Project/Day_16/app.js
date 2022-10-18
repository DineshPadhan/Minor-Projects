let randomNum = parseInt(Math.random() * 99);
console.log(randomNum);
let inputNum = $('input').val();

$('button').click(function () {
    if (randomNum = inputNum) {
        $('.ans').text("Congratulations You Got the Number");
    }else{
        if (inputNum > randomNum) {
            $('.ans').text('Number is too big, please try again');
        }
        else if (inputNum < randomNum) {
            $('.ans').text('Number is too small, please try again');
        }
    }
});
