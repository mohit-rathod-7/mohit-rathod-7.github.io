from project import app
from project.routes import auth, home, calendar, sales, vouchers


app.register_blueprint(home.home,          url_prefix='/')
app.register_blueprint(auth.auth,          url_prefix='/auth')
app.register_blueprint(sales.sales,        url_prefix='/sales')
app.register_blueprint(vouchers.vouchers,  url_prefix='/vouchers')
app.register_blueprint(calendar.calendar,  url_prefix='/calendar')


if __name__ == '__main__':
    app.run(debug=True)
