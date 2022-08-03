$('.profile').click(function(){
    var user_key = $(this).attr('data-user-key');
    var your_key = $(".container").attr('data-your-key');

    var chat_link = Flask.url_for("chat.conversation", {"your_key": your_key, "user_key": user_key});
    
    window.location.href = chat_link;
});