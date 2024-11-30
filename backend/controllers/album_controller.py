from utils.response import json
from models.album import Album

def get_all_albums():
    album = Album.query.all()
    if not album:
        return json(False, 'No photos found', 404)

    album_data = [{'id': p.id, 'album_id': p.album_id, 'title': p.title, 'url': p.url} for p in album]
    return json(True, 'Albums found', 200, album_data)