from flask import jsonify  # type: ignore


def json(success: bool, message: str, status: int, *args, **kwargs):
    return jsonify({'success': success, 'message': message, 'data': kwargs}), status
