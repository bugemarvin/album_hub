from flask import request  # type: ignore
from functools import wraps
from flask_jwt_extended import get_jwt_identity, ExpiredSignatureError, JWTDecodeError  # type: ignore
from utils import json_response

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return json_response(False, 'Token is missing!', 401)

        try:
            identity = get_jwt_identity()
            request.user_id = identity
        except ExpiredSignatureError:
            return json_response(False, 'Token has expired!', 401)
        except JWTDecodeError:
            return json_response(False, 'Invalid token!', 401)
        except Exception as e:
            return json_response(False, f"An error occurred: {str(e)}", 401)

        return f(*args, **kwargs)

    return decorated
