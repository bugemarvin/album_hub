from models.db import db

class Photo(db.Model):
    __tablename__ = 'photos'
    id = db.Column(db.Integer, primary_key=True)
    album_id = db.Column(db.Integer, db.ForeignKey('albums.id'), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    url = db.Column(db.String(255), nullable=False)
    thumbnail_url = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    album = db.relationship('Album', backref=db.backref('photos', lazy=True))

    def save(self):
        db.session.add(self)
        db.session.commit()