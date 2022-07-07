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