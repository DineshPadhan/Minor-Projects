let outer = document.querySelector(".outer")
// let inner = document.querySelector(".inner")
let percent = document.querySelector("span")
let count = 0;
var loading = () => {
    let load = setInterval(animate, 200);
    function animate() {
        if (count == 100) {
            clearInterval();
            outer.classList.remove("active-loder")
            outer.classList.add("active-loder-2")
        } else {
            count = count + 1;
            percent.textContent = count + '%';
            outer.classList.add("active-loder")
            outer.classList.remove("active-loder-2")
        }
    }
}
loading();