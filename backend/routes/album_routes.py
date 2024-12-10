from flask import Blueprint, request  # type: ignore
from controllers.album_controller import (
    get_all_albums,
    get_user_albums,
    get_all_albums_grouped_by_user,
    update_album,
    create_album_for_user
)

album_bp = Blueprint('album_bp', __name__)

@album_bp.route('/albums', methods=['GET'])
def list_all_albums():
    return get_all_albums()


@album_bp.route('/albums/user', methods=['GET'])
def list_user_albums():
    return get_user_albums()


@album_bp.route('/albums/grouped', methods=['GET'])
def list_grouped_albums():
    return get_all_albums_grouped_by_user()


@album_bp.route('/albums/<int:album_id>', methods=['PUT'])
def modify_album(album_id):
    data = request.get_json()
    new_title = data.get("title")
    return update_album(album_id, new_title)


@album_bp.route('/albums', methods=['POST'])
def add_album():
    data = request.get_json()
    title = data.get("title")
    return create_album_for_user(title)
