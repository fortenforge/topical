chrome.runtime.sendMessage({message: "isMusicPlaying"}, function(response) {
  console.log(response);
    if (response.message !== undefined) {
      console.log("ready to play");
      var images = document.getElementsByTagName('img');
    var srcList = [];
    for(var i = 0; i < images.length; i++) {
        srcList.push(images[i].src);
    }
    var htmlText = $("p").text();
    var xmlhttp = new XMLHttpRequest();   // new HttpRequest instance
    var responseText;
    xmlhttp.onreadystatechange=function() {
      if (xmlhttp.readyState==4 && xmlhttp.status==200) {
        responseText = xmlhttp.responseText;
        console.log(responseText);
        chrome.runtime.sendMessage({message : "musicStarted"}, function(response) {
          console.log(responseText);
          var iframe = document.createElement('iframe');
          iframe.setAttribute("style", "position:fixed;bottom:0;right:0;height:80px;border:none;z-index:9999;")
          iframe.src = "https://embed.spotify.com/?uri=spotify:track:" + responseText;
          document.body.insertBefore(iframe, document.body.firstChild);
        });
      }
    }
    //xmlhttp.open("POST", "http://play-hackmit.rhcloud.com/content/", true);
    xmlhttp.open("POST", "http://127.0.0.1:5000/content/"), true;
    xmlhttp.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    console.log(srcList);
    console.log(encodeURIComponent(srcList));
    thing = encodeURIComponent(srcList)
    if(srcList.length == 0) {
      thing = ""
    }
    xmlhttp.send("content=" + encodeURIComponent(htmlText) + "&images=" + thing);
  }
  return;
});
