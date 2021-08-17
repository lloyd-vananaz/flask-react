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


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')
    JWT_TOKEN_LOCATION = ["headers", "cookies"]


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = db_connection_string
    # SQLALCHEMY_DATABASE_URI = os.path.join(basedir, 'app.db')


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite://'


config = {
    'development': DevConfig,
    'testing': TestConfig
}