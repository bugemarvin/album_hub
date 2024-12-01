from flask import Blueprint  # type: ignore
from controllers.user_controller import get_all_users, login, register, logout, reset_password, forgot_password, get_user_profile

user_bp = Blueprint('user_bp', __name__)


@user_bp.route('/users', methods=['GET'])
def list_users():
    return get_all_users()


@user_bp.route('/login', methods=['POST'])
def login_users():
    return login()


@user_bp.route('/register', methods=['POST'])
def register_users():
    return register()


@user_bp.route('/logout', methods=['POST'])
def logout_users():
    return logout()

@user_bp.route('/forgot-password', methods=['GET','POST'])
def forgot_password_users():
    return forgot_password()

@user_bp.route('/reset-password', methods=['GET', 'POST'])
def reset_password_users():
    return reset_password()

@user_bp.route('/profile', methods=['GET', 'PUT'])
def user_profile():
    return get_user_profile()
