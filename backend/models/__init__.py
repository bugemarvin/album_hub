from .blacklist import Blacklist as blacklist
from .db import db
from .user import User
from .album import Album
from .photo import Photo

def check_blacklist(jti):
    return blacklist.is_blacklisted(jti)


def add_to_blacklist(token):
    blacklist.add(token)


def remove_from_blacklist(token):
    blacklist.delete(token)


def clear_blacklist():
    blacklist.delete_all()


def delete_blacklist_token(token):
    blacklist.delete(token)


def blacklist_tokens():
    return blacklist.all()


def blacklist_save():
    blacklist.save()
