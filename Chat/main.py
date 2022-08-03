# Manual imports
from views import chat
from views.app import app


app.register_blueprint(chat.chat,  url_prefix='/chat',  method=['GET', 'POST'])


if __name__ == '__main__':
    app.run(debug=True)
