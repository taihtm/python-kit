from flask import Blueprint, request, flash
from ..service.user_service import add_new_user

bp = Blueprint('user', __name__, url_prefix='/user')


@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        error = None
        username = request.form.get('username', '')
        email = request.form.get('email', '')
        print(email)
        return "Success"
