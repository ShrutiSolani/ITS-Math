from flask import Flask
import mysql.connector, datetime, logging, json_logging, sys
from .home.routes import home_bp
from .fractions.routes import fractions_bp
from .questions_list.routes import choice_bp
from .algebra.routes import algebra_bp
from pythonjsonlogger import jsonlogger



def create_app():
    app = Flask(__name__, instance_relative_config=False)

    # logger = logging.getLogger()
    # logHandler = logging.StreamHandler()
    # formatter = jsonlogger.JsonFormatter()
    # logHandler.setFormatter(formatter)
    # logger.addHandler(logHandler)
    logging.basicConfig(filename = 'UserLog.log', level=logging.INFO, format = '%(asctime)s|%(message)s')
    app.secret_key = 'super secret key'
    log = logging.getLogger('werkzeug')
    log.setLevel(logging.ERROR)
    # app.debug = True
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="ITS"
    )
    app.register_blueprint(home_bp)
    app.register_blueprint(choice_bp)
    app.register_blueprint(fractions_bp)
    app.register_blueprint(algebra_bp)

    return app
