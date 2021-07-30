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
    SQLALCHEMY_DATABASE_URI = db_connection_string # For MySQL
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db') # For SQLite
    SQLALCHEMY_TRACK_MODIFICATIONS = False