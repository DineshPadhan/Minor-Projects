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
        a.preventDefault(); // preventing form from submitting
        fetchFile(hiddeInput.value);
        // console.log(imgTag.src);
    });
    
    function fetchFile(url) {
        // fetching file & returning response as blob
        fetch(url).then(res => res.blob()).then(file => {
            let tempUrl = URL.createObjectURL(file);
            // console.log(tempUrl);
            let aTag = document.createElement("a");
            aTag.href = tempUrl;
            aTag.download = "filename";
            document.body.appendChild(aTag);
            console.log(aTag);
            aTag.click();
            aTag.remove();
        });
    }
    
    
}

