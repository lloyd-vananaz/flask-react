from flask import Blueprint, request
from flask.json import jsonify
from flask_cors.decorator import cross_origin
from flask_login import current_user, login_user, logout_user
from flask_jwt_extended import create_access_token, set_access_cookies, unset_access_cookies

from app.users.models import User
from app.users.forms import LoginUserForm


bp = Blueprint('auths', __name__, url_prefix='/auth')


@bp.route('/login-flask', methods=['POST'])
@cross_origin()
def login_flask():
    if current_user.is_authenticated:
        return jsonify({'message': 'User is already logged in', 'success': 1})

    login_json = request.get_json()
    login_form = LoginUserForm.from_json(login_json)

    if login_form.validate():
        user = User.query.filter_by(username=login_form.username.data).first()
        if user is None or not user.check_password(login_form.password.data):
            return jsonify({'message': 'Invalid username or password', 'success': 0})
        login_user(user, remember=login_form.remember_me.data)
        return jsonify({'message': 'Login successful', 'success': 1})
    else:
        return jsonify({'errors': login_form.errors, 'success': 1})

@bp.route('/logout-flask')
@cross_origin()
def logout_flask():
    logout_user()
    return jsonify({'message': 'Logout successfull', 'success': 1})

@bp.route('/login-without-cookies', methods=['POST'])
@cross_origin()
def login_without_cookies():
    username = request.authorization.username
    password = request.authorization.password
    login_form = LoginUserForm.from_json(username=username, password=password)

    if login_form.validate():
        user = User.query.filter_by(username=login_form.username.data).first()
        if user is None or not user.check_password(login_form.password.data):
            return jsonify({'message': 'Invalid username or password', 'success': 0})
        access_token = create_access_token(identity=login_form.username.data)
        return jsonify({'access_token': access_token, 'success': 1})
    else:
        return jsonify({'errors': login_form.errors, 'success': 0})

@bp.route('/login-with-cookies', methods=['POST'])
@cross_origin()
def login_with_cookies():
    username = request.authorization.username
    password = request.authorization.password
    login_form = LoginUserForm.from_json(username=username, password=password)

    if login_form.validate():
        user = User.query.filter_by(username=login_form.username.data).first()
        if user is None or not user.check_password(login_form.password.data):
            return jsonify({'message': 'Invalid username or password', 'success': 0})
        access_token = create_access_token(identity=login_form.username.data)
        response = jsonify({'message': 'Login successful', 'success': 1})
        set_access_cookies(response, access_token)
        return response
    else:
        return jsonify({'errors': login_form.errors, 'success': 0})

@bp.route('/logout-with-cookies', methods=['POST'])
@cross_origin()
def logout_with_cookies():
    response = jsonify({'message': 'Logout successful', 'success': 1})
    unset_access_cookies(response)
    return response