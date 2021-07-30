from flask import Flask
from flask_cors import CORS # This fixes the error in React app regarding the CORS policy
from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
from config import Config


db = SQLAlchemy()
# migrate = Migrate()


def create_app(config_class=Config):
    app = Flask(
        __name__,
        static_url_path='',
        static_folder='../../react-app/build',
        template_folder='../../react-app/build'
    )
    app.config.from_object(config_class)

    CORS(app)

    db.init_app(app)
    # migrate.init_app(app, db)

    # blueprint registration
    from app.routes import bp as routes_bp
    app.register_blueprint(routes_bp)

    from app.api import bp as api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    return app