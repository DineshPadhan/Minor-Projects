const { response } = require("express")

const urlField = document.querySelector(".field input")
const previewArea = document.querySelector(".preview-area")
const imgTag = previewArea.querySelector(".thumbnail")
const hiddeInput = document.querySelector(".hidden-input")
const downloadBtn = document.querySelector(".download-btn")

urlField.onkeyup = (hiddeInput) => {
    let imgUrl = urlField.value;    //get user entered value
    // console.log(imgTag);
    previewArea.classList.add("active");

    if ((imgUrl.indexOf("https://www.youtube.com/watch?v=") != -1) || (imgUrl.indexOf("youtube.com/watch?v=") != -1)) {  //if url is yt video url
        let vidId = imgUrl.split('v=')[1].substring(0, 11);    //spliting yt url from v= so we get only video Id
        let ytThumbUrl = `https://i.ytimg.com/vi/${vidId}/maxresdefault.jpg`;   //this is video thumbnail url
        imgTag.src = ytThumbUrl;    //passing url inside img src
    } else if (imgUrl.indexOf("https://youtu.be/") != -1) { //if video url is like this
        let vidId = imgUrl.split('be/')[1].substring(0, 11);    //spliting yt url from be/ so we get only video Id
        let ytThumbUrl = `https://i.ytimg.com/vi/${vidId}/maxresdefault.jpg`;   //this is video thumbnail url
        imgTag.src = ytThumbUrl;    //passing url inside img src
    } else if (imgUrl.match(/\.(jpe?g|png|gif|bmp|webp)$/i)) {  //if value is other then yt video url
        imgTag.src = imgUrl;    //passing user entered url inside img src
    } else {
        imgTag.src = "";
        previewArea.classList.remove("active");
    }
    hiddeInput.value = imgTag.src; // passing immg src to hidden input value

    downloadBtn.addEventListener("click", (a) => {
        axios({
            url: imgTag.src,
            method: 'GET',
            ResponseType: 'blob'
        })
            .then((response)=> {
            const url = window.URL.createObjectURL(new Blob[response.data]);

            const link = document.createElement('a');

            link.href = link;

            link.setAttribute('download', 'thumbnail.jpg');

            document.body.appendChild(link);

            link.click();
        });
    });



}

