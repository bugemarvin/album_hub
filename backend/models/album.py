from models.db import db

class Album(db.Model):
    __tablename__ = 'albums'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    
    user = db.relationship('User', backref=db.backref('albums', lazy=True))

    def save(self):
        db.session.add(self)
        db.session.commit()

