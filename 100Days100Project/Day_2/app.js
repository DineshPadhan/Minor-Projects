const slider = document.querySelector(".slider input");
const img = document.querySelector(".slider .images2");
const dragLine = document.querySelector(".slider .dragLine");
slider.oninput = () => {
    let sliderVal = slider.value;
    $(".dragLine").css("left", sliderVal+"%");
    $('.images2').css("width", sliderVal+"%");
}