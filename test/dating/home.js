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

$("#home").addClass("disabled");

function scrollTopAnimated() {
    $(".card-info").scrollTop(0);
}

// SET TIMELINE
const cardInfo = gsap.timeline();
var animationDuration = 1;

// TO OPEN .card-info BOX
$('.swiper-info').click(function(){
    cardInfo
    .from('.card-info', { ease: 'power2.in', duration: animationDuration, y: '100%' })
    .to('.card-info', { ease: 'power2.in', duration: animationDuration, y: '0%'})
    .set('.swiper', { pointerEvents: 'none' })

    TweenLite.to(".card-info", animationDuration, {ease: Back.easeInOutSine, force3D: true, display: 'block' });
    TweenLite.to(".swiper", animationDuration, {ease: Back.easeInOutSine, opacity: '0.8' });
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
