from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    openid = db.Column(db.String(255), unique=True, nullable=False)
    nickname = db.Column(db.String(255), nullable=False)
    avatar_url = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.TIMESTAMP, default=db.func.current_timestamp())

    def __repr__(self):
        return f'<User {self.nickname}>'
