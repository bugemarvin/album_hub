from flask import Blueprint # type: ignore
from controllers.album_controller import get_all_albums

album_bp = Blueprint('album', __name__)

@album_bp.route('/albums', methods=['GET'])
def list_albums():
    return get_all_albums()

