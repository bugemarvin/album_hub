from utils import json_response
from models.album import Album
from models.user import User
from flask_jwt_extended import get_jwt_identity, jwt_required # type: ignore

@jwt_required()
def get_all_albums():
    albums = Album.query.all()
    if not albums:
        return json_response(False, 'No albums found', 404)

    album_data = [{"id": album.id, "title": album.title, "created_at": album.created_at} for album in albums]
    return json_response(True, 'Albums found', 200, album_data)

@jwt_required()
def get_user_albums():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if not user:
        return json_response(False, "User not found", 404)

    albums = Album.query.filter_by(user_id=user_id).all()
    album_list = [{"id": album.id, "title": album.title, "created_at": album.created_at} for album in albums]
    return json_response(True, "Albums found", 200, {"user_id": user.id, "username": user.username, "albums": album_list})


@jwt_required()
def get_all_albums_grouped_by_user():
    users = User.query.all()
    grouped_albums = [{
        "user_id": user.id,
        "username": user.username,
        "albums": [{"id": album.id, "title": album.title, "created_at": album.created_at} for album in user.albums]
    } for user in users]

    return json_response(True, 'Grouped albums', 200, grouped_albums)


@jwt_required()
def update_album(album_id, new_title):
    user_id = get_jwt_identity()
    album = Album.query.filter_by(id=album_id, user_id=user_id).first()
    if not album:
        return json_response(False, "Album not found or does not belong to the user.", 404)

    album.title = new_title
    album.save()
    return json_response(True, "Album updated successfully.", 200, {"id": album.id, "title": album.title})

@jwt_required()
def create_album_for_user(title):
    user_id = get_jwt_identity()
    try:
        new_album = Album(user_id=user_id, title=title)
        new_album.save()
        return json_response(True, "Album created successfully.", 201, {"id": new_album.id, "title": new_album.title})
    except Exception as e:
        return json_response(False, "Failed to create album.", 500, {"error": str(e)})
