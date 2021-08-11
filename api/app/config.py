import os
from dotenv import load_dotenv


basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))
db_connection_string = 'mysql+pymysql://{usr}:{pwd}@{host}/{db}'.format(
    usr = os.environ.get('TODODB_USER'),
    pwd = os.environ.get('TODODB_PWD'),
    host = os.environ.get('TODODB_HOST'),
    db = os.environ.get('TODODB_NAME')
)


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = db_connection_string
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')
    JWT_TOKEN_LOCATION = ["headers", "cookies"]