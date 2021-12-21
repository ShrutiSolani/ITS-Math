from flask import Flask
from .home.routes import home_bp
from .fractions1.routes import fractions1_bp
from .questions_list.routes import choice_bp
from .algebra.routes import algebra_bp
from decouple import config


def create_app():
    app = Flask(__name__, instance_relative_config=False)
    app.secret_key = config('APP_SECRET_KEY')
    app.debug = True
    app.register_blueprint(home_bp)
    app.register_blueprint(choice_bp)
    app.register_blueprint(fractions1_bp)
    app.register_blueprint(algebra_bp)
    return app
