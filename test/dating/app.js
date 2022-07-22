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
    $('.material-icons').css('visibility', 'visible');

    var imgDefer = document.getElementsByTagName('img');

    for (var i = 0; i < imgDefer.length; i++) {
        if (imgDefer[i].getAttribute('data-src')) {
            imgDefer[i].setAttribute('src', imgDefer[i].getAttribute('data-src'));
            imgDefer[i].removeAttribute('data-src');
        }
    }
}

$(window).on('load', function() {
    defer();
});
