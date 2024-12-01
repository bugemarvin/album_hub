from . import response


def json_response(success: bool, message: str, status_code: int, data: dict=None):
    return response.json(success, message, status_code, data or None)