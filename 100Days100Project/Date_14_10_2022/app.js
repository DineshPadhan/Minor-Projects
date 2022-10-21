const button = $(".container button");
const jokeDiv = $(".joke p");

document.addEventListener("DOMContentLoaded", getjock);
// button.addEventListener("click", getjock());

async function getjock() {
    const jokeData = await fetch("https://hindi-jokes-api.onrender.com/jokes?api_key=43e93baacbc58e0fc3749ba1593d",{
        headers:{Accept:"application/json"},
    });
    const jokeObj = await jokeData.json();
    // jokeDiv.innerHtml = jokeObj.jokeContent;
    $(jokeDiv).html(jokeObj.jokeContent);
}