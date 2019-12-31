import connexion
import logging
import os
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from configparser import ConfigParser

db = SQLAlchemy()
cwd = os.getcwd()
ma = Marshmallow()


def create_app(config_filename=None):
    config_parser = ConfigParser(os.environ)
    config_path = os.path.join(cwd, config_filename)
    config_parser.read(config_path)

    logging.basicConfig(level=logging.INFO)
    connexion_app = connexion.App(__name__, specification_dir='openapi/')
    connexion_app.add_api('openapi.yaml', arguments={'title': 'aspect'}, pythonic_params=True)
    application = connexion_app.app

    db_user = config_parser.get('mysql', 'db_user')
    db_password = config_parser.get('mysql', 'db_password')
    db_endpoint = config_parser.get('mysql', 'db_endpoint')
    db_port = config_parser.get('mysql', 'db_port')
    db_name = config_parser.get('mysql', 'db_name')
    application.config[
        'SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://' + db_user + ':' + db_password + '@' + db_endpoint + ':' + db_port + '/' + db_name

    db.init_app(application)
    ma.init_app(application)
    return connexion_app
