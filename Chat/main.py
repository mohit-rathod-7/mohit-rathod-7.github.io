# Manual imports
from views import recs
from views import auth
from views import like
from views import chat
from views import user
from views.app import app
 

app.register_blueprint(recs.recs,  url_prefix='/recs',  method=['GET', 'POST'])
app.register_blueprint(auth.auth,  url_prefix='/auth',  method=['GET', 'POST'])
app.register_blueprint(like.like,  url_prefix='/like',  method=['GET', 'POST'])
app.register_blueprint(chat.chat,  url_prefix='/chat',  method=['GET', 'POST'])
app.register_blueprint(user.user,  url_prefix='/user',  method=['GET', 'POST'])


if __name__ == '__main__':
    app.run(debug=True)
