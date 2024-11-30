from flask import jsonify  # type: ignore


def json(success: bool, message: str, status: int, data: dict = None, **kwargs):
    return jsonify({'success': success, 'message': message, 'data': data}), status
