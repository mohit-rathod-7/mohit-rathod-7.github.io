// TO HIDE|DEFER FONT-TEXT|IMAGES WHILE LOADING PAGE
function defer(){
    var imgDefer = document.getElementsByTagName('img');

    for (var i = 0; i < imgDefer.length; i++) {
        if (imgDefer[i].getAttribute('data-src')) {
            imgDefer[i].setAttribute('src', imgDefer[i].getAttribute('data-src'));
            imgDefer[i].removeAttribute('data-src');
        }
    }

    $('.content').css('visibility', 'visible');
    $('.loader').remove();
}

document.addEventListener("DOMContentLoaded", function(){
    defer();
});

$(window).on('load', function() {
    $('.material-icons').css('visibility', 'visible');
});


// Handle Nav Modal
$("#menu").click(function(){
    $('.nav__modal').css('display', 'flex'); 
    $('#close').css('display', 'block'); 
    $('#menu').css('display', 'none'); 
});

$("#close").click(function(){
    $('.nav__modal').css('display', 'none'); 
    $('#menu').css('display', 'block'); 
    $('#close').css('display', 'none'); 
});
