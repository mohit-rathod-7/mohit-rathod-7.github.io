$(document).ready(function() {
    $(document).on('click', '#like', function() {
        // var count = $(this).attr("data-count");

        req = $.ajax({
            url : "likes.html",
            type : "GET"
        });

        req.done(function(data) {
            console.log(data);
            $(".content").html(data);
        });
    });
});

function scrollTopAnimated() {
    $(".card-info").scrollTop(0);
}

// SET TIMELINE
const cardInfo = gsap.timeline();
var animationDuration = 0.5;

// TO OPEN .card-info BOX
$('.swiper-info').click(function(){
    cardInfo
    .from('.card-info', { ease: 'power2.in', duration: animationDuration, y: '100%' })
    .to('.card-info', { ease: 'power2.in', duration: animationDuration, y: '0%'})
    .set('.swiper', { pointerEvents: 'none' })

    TweenLite.to(".card-info", animationDuration*2, {ease: Back.easeInOutSine, force3D: true, display: 'block' });
    TweenLite.to(".swiper", animationDuration*2, {ease: Back.easeInOutSine, opacity: '0.75' });
})

// TO CLOSE .card-info BOX
$('.card-close .icon').click(function(){
    cardInfo
    .call(scrollTopAnimated())
    .to('.card-info', { ease: 'power2.in', duration: animationDuration, y: '100%' })
    .set('.swiper', { pointerEvents: 'all' })
    
    TweenLite.to(".card-info", animationDuration*2, {ease: Back.easeInOutSine, force3D: true, display: 'none' });
    TweenLite.to(".swiper", animationDuration*2, {ease: Back.easeInOutSine, opacity: '1' });
})

// TO HIDE FONT-TEXT and IMAGES WHILE LOADING PAGE
function deferImages() {
    var imgDefer = document.getElementsByTagName('img');

    for (var i = 0; i < imgDefer.length; i++) {
        if (imgDefer[i].getAttribute('data-src')) {
            imgDefer[i].setAttribute('src',imgDefer[i].getAttribute('data-src'));
        }
    }
}

$(window).on('load', function() {
    $('.material-icons').css('visibility','visible');
    deferImages();
});
