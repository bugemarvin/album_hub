from utils.response import json
from models.photo import Photo

def get_all_photos():
    photos = Photo.query.all()
    if not photos:
        return json(False, 'No photos found', 404)

    photos_data = [{'id': p.id, 'album_id': p.album_id, 'title': p.title, 'url': p.url} for p in photos]
    return json(True, 'Photos found', 200, photos_data)