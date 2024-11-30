from utils import json_response

def register_error_handlers(app):
    @app.errorhandler(404)
    def not_found(error):
        return json_response(False, 'Not found', 404)

    @app.errorhandler(500)
    def internal_error(error):
        return json_response(False, 'Internal server error', 500)
