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

// menu program

var menu_btn = document.getElementById('menu-btn');
var menu_body = document.getElementById('menu-show');
var is_show = false

menu_btn.onclick = function () {
    if (is_show == false) {
        menu_body.style.display = 'flex'
        menu_body.style.scale = '1'
        is_show = true
    }else{
        menu_body.style.display = 'none'
        menu_body.style.scale = '0.8'
        is_show = false
    }
}
window.onresize = function () {
    menu_body.style.display = 'none'
    menu_body.style.scale = '0.8'
    is_show = false
}