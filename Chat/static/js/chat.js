$(function(){
    $("#send").on('click', function(){
        var message = $("#message").val();
        var trimmed_message = message.trim();

        if (trimmed_message != ""){
            var your_username = $("#your_username").val();

            req =  $.ajax({
                url : "/chat/send_message",
                type: "POST",
                data : {'username': your_username, 'message':message}
            });

            req.done(function(){
                $('#message').val('');
                $('#message').css("height", '100%');
            });
        }
        else{
            alert("Message is empty !!!");
            $('#message').val('');
        }
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
    // alert(JSON.stringify(data));
    
    // Set Date
    var d = new Date();
    var month = d.getMonth()+1;
    var day = d.getDate();

    var current_time = d.toLocaleTimeString("en-GB", {hour:'numeric', minute:'numeric', hour12: true});
    var current_date = d.toLocaleDateString("en-GB", {day: 'numeric', month: 'numeric', year: 'numeric'});

    console.log("Current date :", current_date, "Current time :", current_time)

    let messaged_by_me = `
        <ul class="me message_container">
            <li class="message">${data.message}
                <span class="message-timestamp sec-text">${current_time}</span>
            </li>
        </ul>`

    let messaged_received = `
        <ul class="other message_container">
            <li class="message">${data.message}
                <span class="message-timestamp sec-text">${current_time}</span>
            </li>
        </ul>`

    let new_chat_by_me = `
        <div class="chat" data-date="${current_date}">
            <header class="date">Today</header>
            <div class="messages">
                <ul class="me message_container">
                    <li class="message">${data.message}
                        <span class="message-timestamp sec-text">${current_time}</span>
                    </li>
                </ul>
            </div>
        </div>`
    
    let new_chat_received = `
        <div class="chat" data-date="${current_date}">
            <header class="date">Today</header>
            <div class="messages">
                <ul class="other message_container">
                    <li class="message">${data.message}
                        <span class="message-timestamp sec-text">${current_time}</span>
                    </li>
                </ul>
            </div>
        </div>`


    // Get latest chat date
    var latest_chat = $(".chat")[0];

    // For new chat
    if (latest_chat == undefined){
        if ($("#your_username").val() == data.username){
            console.log("new chat sent by me")
            $(".chat_section").prepend(new_chat_by_me);
        }
        else{
            console.log("new chat received")
            $(".chat_section").prepend(new_chat_received);
        }
    }
    // If message sent today
    else if (current_date == latest_chat.getAttribute("data-date")){
        // Message sent by me
        if ($("#your_username").val() == data.username){
            $(".chat .messages")[0].innerHTML += messaged_by_me;
        }
        // Message received by me
        else{
            $(".chat .messages")[0].innerHTML += messaged_received;
        }
    }
    // If message sent any other day after last chat date
    else if (day >= latest_chat.getAttribute("data-date").substring(0, 2)){
        if ($("#your_username").val() == data.username){
            console.log("new chat sent by me")
            $(".chat_section").prepend(new_chat_by_me);
        }
        else{
            console.log("new chat received")
            $(".chat_section").prepend(new_chat_received);
        }
    }
});
