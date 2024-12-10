from models.db import db
from sqlalchemy.orm import relationship # type: ignore


class Blacklist(db.Model):
    __tablename__ = 'blacklist'
    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(255), nullable=False)
    blacklisted_on = db.Column(db.DateTime, server_default=db.func.now())
    jti = db.Column(db.String(255), nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship('User', backref='blacklisted_tokens', lazy=True)

    @classmethod
    def is_blacklisted(cls, jti):
        return cls.query.filter_by(jti=jti).first() is not None

    @classmethod
    def add(cls, token):
        jti = token.get('jti')
        user_id = token.get('sub')
        if not user_id:
            raise ValueError("Token does not contain 'sub' (identity).")
        new_blacklist_token = cls(token=f'{token}', jti=jti, user_id=user_id)
        db.session.add(new_blacklist_token)
        db.session.commit()

    @classmethod
    def delete(cls, token):
        jti = token['jti']
        blacklist_token = cls.query.filter_by(jti=jti).first()
        if blacklist_token:
            db.session.delete(blacklist_token)
            db.session.commit()

    @classmethod
    def delete_all(cls):
        cls.query.delete()
        db.session.commit()

    @classmethod
    def all(cls):
        return cls.query.all()

    @classmethod
    def save(cls):
        db.session.commit()

    def __repr__(self):
        return f"<Blacklist {self.jti}>"
