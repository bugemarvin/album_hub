from flask import Blueprint # type: ignore
from routes.user_routes import user_bp
from routes.album_routes import album_bp
from routes.photo_routes import photo_bp
from routes.main_routes import main_bp

def register_routes(app):
    app.register_blueprint(main_bp, url_prefix='/')
    app.register_blueprint(user_bp, url_prefix='/api/v1/')
    app.register_blueprint(album_bp, url_prefix='/api/v1/')
    app.register_blueprint(photo_bp, url_prefix='/api/v1/')
