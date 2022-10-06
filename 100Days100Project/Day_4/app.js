setInterval(() => {
    let time = new Date();
    let sec = time.getSeconds();
    let min = time.getMinutes();
    let hr = time.getHours();
    let day = "";
    if (hr > 12) {
        hr = hr - 12
        day = "PM"
    }
    else{
        day = "Am"
    }
    if (sec < 10) {
        sec = "0" + sec
    }
    if (min < 10) {
        min = "0" + min
    }
    if (hr < 10) {
        hr = "0" + hr
    }
    $(".display").text(`${hr}:${min}:${sec} ${day}`);

    // $(".display").text(time.toLocaleTimeString());
});