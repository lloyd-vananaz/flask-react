from flask import Blueprint, request
from flask.json import jsonify
from flask_cors.decorator import cross_origin
from flask_login import current_user

from app import db
from app.users.models import User
from app.users.forms import RegisterUserForm


bp = Blueprint('user', __name__, url_prefix='/api/user')


@bp.route('/register', methods=['POST'])
@cross_origin()
def register():
    if current_user.is_authenticated:
        return jsonify({'message': 'User is already logged in'})

    register_json = request.get_json()
    register_form = RegisterUserForm.from_json(register_json)

    if register_form.validate():
        user = User(username=register_form.username.data, email=register_form.email.data)
        user.set_password(register_form.password.data)
        db.session.add(user)
        db.session.commit()
        return jsonify({'message': 'Registration successfull'})
    else:
        return jsonify({'error': register_form.errors})