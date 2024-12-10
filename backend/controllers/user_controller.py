import datetime
from utils import json_response
from models import User
from flask import request, url_for  # type: ignore
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, get_jwt  # type: ignore
from configs.config import Config
from marshmallow.exceptions import ValidationError  # type: ignore
from middlewares.register_validations import register_schema
from werkzeug.security import generate_password_hash, check_password_hash  # type: ignore
from models.blacklist import Blacklist


def generate_password(password):
    return generate_password_hash(password)


def check_password(password, password_hash):
    return check_password_hash(password_hash, password)


def check_user_online(user):
    online = (
        "online" if user.is_online else "offline"
    )
    return online


@jwt_required()
def get_all_users():
    users = User.query.all()
    if not users:
        return json_response(False, 'No users found', 404)

    users_data = [{'id': u.id, 'first_name': u.first_name, 'last_name': u.last_name,
                   'username': u.username, 'email': u.email, 'online': check_user_online(u)} for u in users]
    return json_response(True, 'Users found', 200, {'users': users_data})


def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return json_response(False, 'Email and password are required', 400)

    user = User.query.filter_by(email=email).first()
    if user and check_password(password, user.password):
        token = create_access_token(identity=user.id, fresh=True, expires_delta=datetime.timedelta(
            seconds=Config.JWT_EXPIRATION))
        user.is_online = True
        user.save()
        return json_response(True, 'Login successful', 200, {'token': token})

    return json_response(False, 'Invalid credentials', 401)


def register():
    try:
        data = register_schema.load(request.json)
    except ValidationError as err:
        return json_response(False, err.messages, 400)

    username = data['username']
    email = data['email']
    password = data['password']
    password_confirm = data['password_confirm']

    if password != password_confirm:
        return json_response(False, 'Passwords do not match', 400)

    password = generate_password_hash(password)
    user = User.query.filter_by(email=email).first(
    ) or User.query.filter_by(username=username).first()
    if user:
        return json_response(False, 'User already exists', 400)

    new_user = User(username=username, email=email, password=password)
    token = create_access_token(identity=new_user.id, fresh=True,
                                expires_delta=datetime.timedelta(seconds=Config.JWT_EXPIRATION))
    new_user.is_online = True
    new_user.save()
    return json_response(True, 'User created successfully', 200, {'token': token})


@jwt_required()
def logout():
    user_id = get_jwt_identity()
    if not user_id:
        return json_response(False, "Invalid or missing token", 401)
    user = User.query.get(user_id)
    if not user:
        return json_response(False, "User not found", 404)
    token = get_jwt()
    jti = token.get('jti')
    if Blacklist.is_blacklisted(jti):
        return json_response(False, "Token already expired", 401)
    Blacklist.add(get_jwt())
    user.is_online = False
    user.save()
    return json_response(True, "Logout successful", 200)


def forgot_password():
    data = request.json
    email = data.get('email')

    if not email:
        return json_response(False, "Email is required", 400)

    user = User.query.filter_by(email=email).first()
    if not user:
        return json_response(False, "User not found", 404)

    reset_token = create_access_token(
        identity=user.id, expires_delta=datetime.timedelta(minutes=15))

    reset_url = url_for('user_bp.reset_password_users',
                        token=reset_token, _external=True)
    return json_response(True, "Password reset email sent", 200)


@jwt_required()
def reset_password():
    user_id = get_jwt_identity()
    data = request.json

    new_password = data.get('new_password')
    confirm_password = data.get('confirm_password')

    if not new_password or not confirm_password:
        return json_response(False, "Both password fields are required", 400)

    if new_password != confirm_password:
        return json_response(False, "Passwords do not match", 400)

    user = User.query.get(user_id)
    if not user:
        return json_response(False, "User not found", 404)

    user.password = generate_password_hash(new_password)
    user.save()

    return json_response(True, "Password updated successfully", 200)


@jwt_required()
def get_user_profile():
    user_id = get_jwt_identity()
    if not user_id:
        return json_response(False, "Invalid token, no user ID found", 400)
    
    user = User.query.get(user_id)
    if not user:
        return json_response(False, "User not found", 404)
    
    profile_data = {
        "id": user.id,
        "username": user.username,
        "email": user.email,
        "created_at": user.created_at,
    }
    return json_response(True, 'User profile found', 200, {"profile": profile_data})

