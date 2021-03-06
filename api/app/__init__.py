from flask import Flask
from flask_cors import CORS # This fixes the error in React app regarding the CORS policy
from flask_jwt_extended import JWTManager
import wtforms_json

from app.config import config
from app.core import db, migrate, login_manager


jwt = JWTManager()


def create_app(config_name, built_react_path=None):
    app = Flask(
        __name__,
        static_url_path='',
        static_folder=built_react_path,
        template_folder=built_react_path
    )
    app.config.from_object(config[config_name])

    CORS(app)
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    jwt.init_app(app)

    wtforms_json.init()

    # blueprint registration
    from app.routes import bp as routes_bp
    app.register_blueprint(routes_bp)

    from app.api.auths import bp as api_auth_bp
    app.register_blueprint(api_auth_bp)

    from app.api.users import bp as api_user_bp
    app.register_blueprint(api_user_bp)

    from app.api.tasks import bp as api_task_bp
    app.register_blueprint(api_task_bp)

    return app