from app import db

class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    couple_id = db.Column(db.Integer, db.ForeignKey('couple.id'), nullable=False)
    image_url = db.Column(db.String(255), nullable=False)
    uploaded_at = db.Column(db.TIMESTAMP, default=db.func.current_timestamp())

    couple = db.relationship('Couple', backref='images')

    def __repr__(self):
        return f'<Image {self.image_url}>'
