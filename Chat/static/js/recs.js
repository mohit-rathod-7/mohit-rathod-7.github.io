$(document).on('click', '#like', function() {
    req = $.ajax({
        url : Flask.url_for('recs.like'),
        type : "GET"
    });

    req.done(function(data) {
        // console.log(data);
        console.log("LIKED");
        $(".content").html(data);
    });
});

$(document).on('click', '#dislike', function() {
    req = $.ajax({
        url : Flask.url_for('recs.dislike'),
        type : "GET"
    });

    req.done(function(data) {
        // console.log(data);
        console.log("DISLIKED");
        $(".content").html(data);
    });
});
