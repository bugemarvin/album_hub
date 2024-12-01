from models.db import db

class Photo(db.Model):
    __tablename__ = 'photos'
    id = db.Column(db.Integer, primary_key=True)
    album_id = db.Column(db.Integer, db.ForeignKey('albums.id'), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    url = db.Column(db.String(255), nullable=False)
    
    def save(self):
        db.session.add(self)
        db.session.commit()