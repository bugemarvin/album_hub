from flask import Blueprint, request  # type: ignore
from controllers.photo_controller import (
    get_photos_by_album,
    create_photo,
    update_photo,
    delete_photo
)

photo_bp = Blueprint('photo_bp', __name__)

@photo_bp.route('/photos/<int:album_id>', methods=['GET'])
def list_photos_in_album(album_id):
    return get_photos_by_album(album_id)

@photo_bp.route('/photos/<int:album_id>', methods=['POST'])
def add_photo_to_album(album_id):
    data = request.get_json()
    title = data.get("title")
    url = data.get("url")
    thumbnail_url = data.get("thumbnail_url")
    return create_photo(album_id, title, url, thumbnail_url)

@photo_bp.route('/photos/<int:photo_id>', methods=['PUT'])
def update_photo_route(photo_id):
    data = request.get_json()
    title = data.get("title")
    url = data.get("url")
    thumbnail_url = data.get("thumbnail_url")
    return update_photo(photo_id, title, url, thumbnail_url)

@photo_bp.route('/photos/<int:photo_id>', methods=['DELETE'])
def delete_photo_route(photo_id):
    return delete_photo(photo_id)
