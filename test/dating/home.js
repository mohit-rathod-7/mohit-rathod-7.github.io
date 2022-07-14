$(document).ready(function() {
    $(document).on('click', '#like', function() {
        console.log("LIKED");
    });

    $("#dislike").click(function(){
        console.log("DISLIKED");
    });
});


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


const cardInfo = gsap.timeline();
var animationDuration = 0.5;

$('.swiper-info').click(function(){
    cardInfo
    .from('.card-info', { ease: 'power2.in', duration: animationDuration, y: '100%', stagger: 0.75 })
    .to('.card-info', { ease: 'power2.in', duration: animationDuration, y: '0%'})

    TweenLite.to(".card-info", animationDuration, {ease: Back.easeInOutSine, force3D: true, display: 'block' });
})


$('.card-close .icon').click(function(){
    cardInfo
    .to('.card-info', { ease: 'power2.in', duration: animationDuration, y: '100%' })

    TweenLite.to(".card-info", animationDuration, {ease: Back.easeInOutSine, force3D: true, display: 'none' });
})
