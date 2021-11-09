from flask import Flask
import os
import mysql.connector, datetime, logging, json_logging, sys
from .home.routes import home_bp
from .fractions1.routes import fractions1_bp
from .questions_list.routes import choice_bp
from .algebra.routes import algebra_bp
# from .home.routes import page_not_found
from pythonjsonlogger import jsonlogger



def create_app():
    app = Flask(__name__, instance_relative_config=False)

    # logger = logging.getLogger()
    # logHandler = logging.StreamHandler()
    # formatter = jsonlogger.JsonFormatter()
    # logHandler.setFormatter(formatter)
    # logger.addHandler(logHandler)
    if 'DYNO' in os.environ:
        app.logger.addHandler(logging.StreamHandler(sys.stdout))
        logging.basicConfig(filename = 'UserLog.log', level=logging.INFO, format = '%(asctime)s|%(message)s')
    app.secret_key = 'super secret key'
    log = logging.getLogger('werkzeug')
    log.setLevel(logging.ERROR)
    app.logger.addHandler(logging.StreamHandler(sys.stdout))
    app.logger.setLevel(logging.ERROR)
    # app1.debug = True
    mydb = mysql.connector.connect(
	    host = "sql6.freesqldatabase.com",
	    user = "sql6449635",
	    database = "sql6449635",
	    password ="EH7dFtDVqR",
	    port = "3306"
	)
    
    app.register_blueprint(home_bp)
    app.register_blueprint(choice_bp)
    app.register_blueprint(fractions1_bp)
    app.register_blueprint(algebra_bp)
    # app.register_error_handler(500,page_not_found)

    return app
