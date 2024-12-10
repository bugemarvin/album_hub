from models.db import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(120), nullable=True)
    last_name = db.Column(db.String(120), nullable=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(20), nullable=True)
    website = db.Column(db.String(255), nullable=True)
    bio = db.Column(db.String(255), nullable=True)
    avatar = db.Column(db.String(255), nullable=True)
    image = db.Column(db.String(255), nullable=True)
    location = db.Column(db.String(255), nullable=True)
    is_admin = db.Column(db.Boolean, default=False)
    is_active = db.Column(db.Boolean, default=True)
    is_verified = db.Column(db.Boolean, default=False)
    is_online = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    address = db.Column(db.JSON, nullable=True)
    company = db.Column(db.JSON, nullable=True)
    # albums = db.relationship('Album', backref='users', lazy=True)

    def save(self):
        db.session.add(self)
        db.session.commit()
