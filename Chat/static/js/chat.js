$(function(){
    $("#send").on('click', function(){
        var message = $("#message").val();
        var your_username = $("#your_username").val();

        req =  $.ajax({
            url : "/chat/send_message",
            type: "POST",
            data : {'username': your_username, 'message':message}
        });

        req.done(function(){
            $('#message').val('');
        });
    });
});

// Enable pusher logging - don't include this in production
Pusher.logToConsole = true;

var pusher = new Pusher('f1d4aad8ba9309f28a05', {
    cluster: 'ap2',
    encrypted: true
});

var channel = pusher.subscribe('my-channel');

channel.bind('new-message', function(data){
    let messaged_by_me = `
        <ul class="me message_container">
            <li class="message">${data.message}</li>
        </ul>`

    let messaged_by_other = `
        <ul class="other message_container">
            <li class="message">${data.message}</li>
        </ul>`

    var d = new Date();
    var month = d.getMonth()+1;
    var day = d.getDate();
    
    var current_date = ((''+day).length<2 ? '0' : '') + day + '/' +
    ((''+month).length<2 ? '0' : '') + month + '/' +
    d.getFullYear()
    
    // alert(JSON.stringify(data));

    var latest_chat = $(".chat")[0];
    var latest_chat_date = latest_chat.getAttribute("data-date");

    if (current_date == latest_chat_date){
        if ($("#your_username").val() == data.username){
            $(".chat .messages")[0].innerHTML += messaged_by_me;
        }
        else{
            $(".chat .messages")[0].innerHTML += messaged_by_other;
        }
    }
});