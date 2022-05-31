from flask import Flask
from flask_pytest_example.handlers.routes import configure_routes
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
csrf = CSRFProtect(app)
csrf.init_app(app)

configure_routes(app)

if __name__ == '__main__':
    app.run()
