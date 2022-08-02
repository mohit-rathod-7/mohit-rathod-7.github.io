function next(page_num){
    req = $.ajax({
        url : "page" + page_num + ".html",
        type : "GET"
    });

    req.done(function(data){
        $(".content").html(data);
    });
}

function next_url(page_name) {
    req = $.ajax({});

    req.done(function(){
        window.location.href = page_name + ".html";
    });
}
