const weatherApiKey = "d2d2d46b5b27c554067ac1b6954e4e30";

const main = document.getElementById('main');
const form = document.getElementById('form');
const search = document.getElementsByClassName('search');

const url = (city) => `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${weatherApiKey}`;


async function getWeatherByLocation(city) {

    const resp = await fetch(url(city), {
        origin: "cros"
    });
    const respData = await resp.json();

    addWeatherToPage(respData);

}

function addWeatherToPage(data) {
    const temp = Ktoc(data.main.temp);

    const weather = document.createElement('div')
    weather.classList.add('weather');

    weather.innerHTML = `<h2><img src="https://openweathermap.org/img/wn/${data.weather[0].icon}@2x.png" /> ${temp}°C <img src="https://openweathermap.org/img/wn/${data.weather[0].icon}@2x.png" /></h2>
          <small>${data.weather[0].main}</small>
          
          `;


    //   cleanup 
    main.innerHTML = "";
    main.appendChild(weather);
};


function Ktoc(K) {
    return Math.floor(K - 273.15);
}



form.addEventListener('submit', (e) => {
    e.preventDefault();

    const city = search.value;

    if (city) {
        getWeatherByLocation(city)
    }

});


//  google place suggection
   