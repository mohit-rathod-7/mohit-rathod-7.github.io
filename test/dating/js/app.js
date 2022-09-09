$(document).ready(function() {
    $(document).on('click', '#like', function() {
        req = $.ajax({
            url : "card.html",
            type : "GET"
        });

        req.done(function(data) {
            // console.log(data);
            $(".content").html(data);
        });
    });
});

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
