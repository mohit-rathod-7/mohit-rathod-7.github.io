from flask import Blueprint, render_template, request, jsonify
import pusher


chat = Blueprint('chat', __name__)


@chat.route('/')
def home():
    return render_template("home.html")


@chat.route('/<your_key>-<user_key>', methods=['GET', 'POST'])
def conversation(your_key, user_key):

    return render_template("chat.html", your_username="mohit")


@chat.route('/send_message', methods=['POST'])
def send_message():
    pusher_client = pusher.Pusher(
        app_id='1457548',
        key='f1d4aad8ba9309f28a05',
        secret='d33c49e7dbf06ccd0d67',
        cluster='ap2',
        ssl=True
    )

    try:
        username = request.form['username']
        message = request.form['message']

        pusher_client.trigger('my-channel', 'new-message', {'username':username, 'message': message})

        return jsonify({'result': 'success'})
    except:
        return jsonify({'result': 'failure'})
