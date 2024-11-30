from models import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    phone = db.Column(db.String(20), nullable=True)
    location = db.Column(db.String(255), nullable=True)
    timezone = db.Column(db.String(50), nullable=True)
    bio = db.Column(db.String(255), nullable=True)
    avatar = db.Column(db.String(255), nullable=True)
    image = db.Column(db.String(255), nullable=True)
    cover = db.Column(db.String(255), nullable=True)
    is_admin = db.Column(db.Boolean, default=False)
    is_active = db.Column(db.Boolean, default=True)
    is_verified = db.Column(db.Boolean, default=False)
    is_public = db.Column(db.Boolean, default=True)
    is_online = db.Column(db.Boolean, default=False)
    last_seen = db.Column(db.DateTime, nullable=True)
    last_active = db.Column(db.DateTime, nullable=True)
    last_login = db.Column(db.DateTime, nullable=True)
    last_logout = db.Column(db.DateTime, nullable=True)
    
