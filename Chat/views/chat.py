from flask import Blueprint, render_template, request, jsonify
import pusher


chat = Blueprint('chat', __name__)

pusher_client = pusher.Pusher(
    app_id='1457548',
    key='f1d4aad8ba9309f28a05',
    secret='d33c49e7dbf06ccd0d67',
    cluster='ap2',
    ssl=True
)

nav_data = {
    "disabled": {
        "home": "",
        "like": "",
        "chat": "disabled",
        "user": "",
    },
    
    "icon": {
        "home": "outlined",
        "like": "outlined",
        "chat": "filled",
        "user": "outlined",
    }
}


@chat.route('/')
def home():
    return render_template("chat/home.html", nav_data=nav_data)


@chat.route('/<your_key>/<user_key>', methods=['GET', 'POST'])
def conversation(your_key, user_key):
    if your_key == user_key:
        return ""
    elif your_key == "0001":
        user = {
            "username": "user1",
            "fullname": "User 1",
            "channel_name": "_1_2"
        }
    elif your_key == "0002":
        user = {
            "username": "user2",
            "fullname": "User 2",
            "channel_name": "_1_2"
        }
    elif your_key == "0003":
        user = {
            "username": "user3",
            "fullname": "User 3",
            "channel_name": "_3_4"
        }
    elif your_key == "0004":
        user = {
            "username": "user4",
            "fullname": "User 4",
            "channel_name": "_3_4"
        }
    return render_template("chat/chat.html", details=user, nav_data=nav_data)


@chat.route('/send_message', methods=['POST'])
def send_message():
    try:
        USERNAME = request.form['username']
        MESSAGE = request.form['message']
        CHANNEL_NAME = request.form['channel_name']

        pusher_client.trigger(CHANNEL_NAME, 'new-message', {'username':USERNAME, 'message': MESSAGE})

        return jsonify({'result': 'success'})
    except:
        return jsonify({'result': 'failure'})
