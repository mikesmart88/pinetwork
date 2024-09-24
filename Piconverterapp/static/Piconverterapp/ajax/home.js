// home javascript programs

// info program

"use strict"

var body = document.getElementById('info');
var okay_btn = document.getElementById('okay-btn');
body.style.display = 'none';


window.addEventListener('load', function () {
   setTimeout(() => {
    body.style.display = 'flex';
   }, 500);
})


okay_btn.onclick = function() {
    body.style.display = 'none';
}