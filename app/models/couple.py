from app import db

class Couple(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user1_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user2_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created_at = db.Column(db.TIMESTAMP, default=db.func.current_timestamp())

    user1 = db.relationship('User', foreign_keys=[user1_id], backref='couple1')
    user2 = db.relationship('User', foreign_keys=[user2_id], backref='couple2')

    def __repr__(self):
        return f'<Couple {self.user1.nickname} & {self.user2.nickname}>'
