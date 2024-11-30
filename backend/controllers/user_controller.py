from utils.response import json
from models.user import User

def get_all_users():
    users = User.query.all()
    if not users:
        return json(False, 'No users found', 404)

    users_data = [{'id': u.id, 'name': u.name, 'username': u.username, 'email': u.email} for u in users]
    return json(True, 'Users found', 200, users_data)
