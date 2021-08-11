from flask import (
    Blueprint,
    render_template
)


bp = Blueprint('routes', __name__)


@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/login')
def login():
    return render_template('index.html')

@bp.route('/register')
def register():
    return render_template('index.html')