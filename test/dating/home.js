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


const sideNav = gsap.timeline();

$('.more').click(function(){
    sideNav
    .from('.card-info', { ease: 'power2.in', duration: 1, y: '100%', stagger: 0.15 })

    TweenLite.to(".card-info", 0.5, {ease: Back.easeInOutSine, force3D: true, x: '0%', display: 'block' });
})
