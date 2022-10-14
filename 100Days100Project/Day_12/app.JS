let count = $(".counter").text();
let plus = $(".fa-plus");
let minus = $(".fa-minus");
let restart = $(".restart");
let start = $(".start");


$(plus).click(function (e) {
    e.preventDefault();
    count++
    // console.log(count);
    if (count >= 00 && count <=9) {
        $('.counter').html("0" + count);
    } else {
        $('.counter').html(count);
    }
});
$(minus).click(function (e) {
    e.preventDefault();
    count--
    if (count < 00) {
        count = 00;
        $('.counter').html(count);
    } else {
        // console.log(count);
        if (count >= 00 && count <= 9) {
            $('.counter').html("0" + count);
        } else {
            $('.counter').html(count);
        }
    }
});

$(restart).click(function (e) {
    e.preventDefault();
    count = 00;
    $('.counter').html(count);
});

$(start).click(function (e) {
    e.preventDefault();
    setInterval(() => {
        count--;
        if (count < 00) {
            count = 00;
            $('.counter').html(count);
        } else {
            // console.log(count);
            if (count >= 00 && count <= 9) {
                $('.counter').html("0" + count);
            } else {
                $('.counter').html(count);
            }
        }
        if (count == 00) {
            // $(start).removeAttrs('disabled');
            // $(start).removeAttr('disabled');
            location.reload();
        }
    }, 1000);
    $(start).attr('disabled', 'disabled');
});