from models.album import Album
from utils import json_response
from models.photo import Photo
from flask_jwt_extended import get_jwt_identity, jwt_required  # type: ignore


@jwt_required()
def get_photos_by_album(album_id):
    """
    Fetches all photos belonging to a specific album.
    """
    album = Album.query.get(album_id)
    if not album:
        return json_response(False, "Album not found", 404)

    photos = Photo.query.filter_by(album_id=album_id).all()
    photo_list = [
        {
            "id": photo.id,
            "title": photo.title,
            "url": photo.url,
            "thumbnail_url": photo.thumbnail_url,
            "created_at": photo.created_at
        }
        for photo in photos
    ]
    return json_response(True, "Photos found", 200, {
        "album_id": album.id,
        "album_title": album.title,
        "photos": photo_list
    })


@jwt_required()
def create_photo(album_id, title, url, thumbnail_url):
    """
    Adds a new photo to a specific album.
    """
    user_id = get_jwt_identity()
    album = Album.query.get(album_id)

    if not album:
        return json_response(False, "Album not found", 404)

    if album.user_id != user_id:
        return json_response(False, "Unauthorized to add photos to this album", 403)

    try:
        new_photo = Photo(
            album_id=album_id,
            title=title,
            url=url,
            thumbnail_url=thumbnail_url
        )
        new_photo.save()
        return json_response(True, "Photo created successfully", 201, {
            "photo": {
                "id": new_photo.id,
                "title": new_photo.title,
                "url": new_photo.url,
                "thumbnail_url": new_photo.thumbnail_url,
                "created_at": new_photo.created_at
            }
        })
    except Exception as e:
        return json_response(False, "Failed to create photo", 500, {"error": str(e)})
    
@jwt_required()
def update_photo(photo_id, title=None, url=None, thumbnail_url=None):
    """
    Updates a photo's details. Only the photo's owner or the user can update the photo.
    """
    user_id = get_jwt_identity()
    photo = Photo.query.get(photo_id)
    
    if not photo:
        return json_response(False, "Photo not found", 404)
    
    album = Album.query.get(photo.album_id)
    if album.user_id != user_id:
        return json_response(False, "Unauthorized to update this photo", 403)
    
    if title:
        photo.title = title
    if url:
        photo.url = url
    if thumbnail_url:
        photo.thumbnail_url = thumbnail_url
    
    try:
        photo.save()
        return json_response(True, "Photo updated successfully", 200, {
            "photo": {
                "id": photo.id,
                "title": photo.title,
                "url": photo.url,
                "thumbnail_url": photo.thumbnail_url,
                "created_at": photo.created_at
            }
        })
    except Exception as e:
        return json_response(False, "Failed to update photo", 500, {"error": str(e)})

@jwt_required()
def delete_photo(photo_id):
    """
    Deletes a photo. Only the photo's owner can delete the photo.
    """
    user_id = get_jwt_identity()
    photo = Photo.query.get(photo_id)
    
    if not photo:
        return json_response(False, "Photo not found", 404)
    
    album = Album.query.get(photo.album_id)
    if album.user_id != user_id:
        return json_response(False, "Unauthorized to delete this photo", 403)
    
    try:
        photo.delete()
        return json_response(True, "Photo deleted successfully", 200)
    except Exception as e:
        return json_response(False, "Failed to delete photo", 500, {"error": str(e)})

