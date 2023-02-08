// TO HIDE|DEFER FONT-TEXT|IMAGES WHILE LOADING PAGE
function defer(){
    var imgDefer = document.getElementsByTagName('img');

    for (var i = 0; i < imgDefer.length; i++) {
        if (imgDefer[i].getAttribute('data-src')) {
            imgDefer[i].setAttribute('src', imgDefer[i].getAttribute('data-src'));
            imgDefer[i].removeAttribute('data-src');
        }
    }

}

document.addEventListener("DOMContentLoaded", function(){
    defer();
});

$(window).on('load', function() {
    $('.material-icons').css('visibility', 'visible');
    $('.content').css('visibility', 'visible');
    $('.loader').remove();
});

$('input[type="text"], input[type="password"], textarea').focus( function() {
    $('.navbar__bottom').hide();
    $('.navbar__dummy').hide();
    $('.content').css('bottom', 0);
});

$('input[type="text"], input[type="password"], textarea').blur( function() {
    $('.navbar__bottom').show();
    $('.navbar__dummy').show();
    $('.content').css('bottom', '6rem');
});

$('.sidebar__icons .closed').on('click', function() {
    $('.sidebar__icons .closed').css('display', 'none');
    
    setTimeout(function(){
        $('.sidebar__links .label').css('display', 'none');
    }, 200)
    
    $('.sidebar__icons .opened').css('display', 'block');
    $('.sidebar').css('width', '6.4rem');
    $('.container .main').css('margin-left', '6.4rem');
});

$('.sidebar__icons .opened').on('click', function() {
    $('.sidebar__icons .closed').css('display', 'block');
    
    setTimeout(function(){
        $('.sidebar__links .label').css('display', 'block');
    }, 200)
    
    $('.sidebar__icons .opened').css('display', 'none');
    $('.sidebar').css('width', '16.4188rem');
    $('.container .main').css('margin-left', '16.4188rem');
});