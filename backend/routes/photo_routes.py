from flask import Blueprint # type: ignore
from controllers.photo_controller import get_all_photos

photo_bp = Blueprint('photo', __name__)

@photo_bp.route('/photos', methods=['GET'])
def list_photos():
    return get_all_photos()

