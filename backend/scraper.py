import requests
import random
import string
import csv
from app import app
from models.db import db
from models import User, Album, Photo

def generate_password(length=10):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for i in range(length))

def create_user(user_data):
    with app.app_context():
        existing_user = User.query.filter_by(email=user_data['email']).first()
        if existing_user:
            print(f"User {user_data['name']} already exists in the database.")
            return existing_user

        password = generate_password()

        new_user = User(
            first_name=user_data['name'].split()[0],
            last_name=user_data['name'].split()[1] if len(user_data['name'].split()) > 1 else '',
            username=user_data['username'],
            email=user_data['email'],
            password=password,
            phone=user_data['phone'],
            website=user_data['website'],
            company=user_data['company'],
            address=user_data['address'],
        )

        new_user.save()
        print(f"User {new_user.first_name} {new_user.last_name} created with password: {password}")

        return new_user

def create_album(album_data, user_id):
    with app.app_context():
        existing_album = Album.query.filter_by(user_id=user_id, title=album_data['title']).first()
        if existing_album:
            print(f"Album '{album_data['title']}' already exists.")
            return existing_album

        new_album = Album(
            user_id=user_id,
            title=album_data['title'],
        )

        new_album.save()
        print(f"Album '{new_album.title}' created.")

        return new_album

def create_photos(photo_data, album_id):
    with app.app_context():
        existing_photo = Photo.query.filter_by(album_id=album_id, title=photo_data['title']).first()
        if existing_photo:
            print(f"Photo '{photo_data['title']}' already exists.")
            return existing_photo

        new_photo = Photo(
            album_id=album_id,
            title=photo_data['title'],
            url=photo_data['url'],
            thumbnail_url=photo_data['thumbnailUrl']
        )

        new_photo.save()
        print(f"Photo '{new_photo.title}' created.")

        return new_photo

def save_user_to_csv(user_data):
    with open('users.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([user_data['email'], user_data['name'], user_data['password']])

def scrape_and_save_data():
    user_api_url = 'https://jsonplaceholder.typicode.com/users'
    album_api_url = 'https://jsonplaceholder.typicode.com/albums'
    photos_api_url = 'https://jsonplaceholder.typicode.com/photos'

    user_response = requests.get(user_api_url)
    users = user_response.json()

    for user_data in users:
        user = create_user(user_data)

        save_user_to_csv({
            'email': user_data['email'],
            'name': user_data['name'],
            'password': user.password
        })

        album_response = requests.get(f"{album_api_url}?userId={user_data['id']}")
        albums = album_response.json()

        for album_data in albums:
            album = create_album(album_data, user.id)

            photo_response = requests.get(f"{photos_api_url}?albumId={album_data['id']}")
            photos = photo_response.json()

            for photo_data in photos:
                create_photos(photo_data, album.id)

if __name__ == '__main__':
    with app.app_context():
        scrape_and_save_data()
