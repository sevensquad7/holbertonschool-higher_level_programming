const painted = document.querySelector('#red_header');
painted.addEventListener('click', colorRed);
function colorRed() {
    $('header').css('color','#FF0000')
}
