from app import db

class LoveLetterReply(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    letter_id = db.Column(db.Integer, db.ForeignKey('love_letter.id'), nullable=False)
    sender_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    content = db.Column(db.Text, nullable=False)
    sent_at = db.Column(db.TIMESTAMP, default=db.func.current_timestamp())
    status = db.Column(db.Enum('sent', 'read', 'deleted'), default='sent')

    letter = db.relationship('LoveLetter', backref='replies')
    sender = db.relationship('User', foreign_keys=[sender_id])

    def __repr__(self):
        return f'<LoveLetterReply {self.sender.nickname} replied to {self.letter.sender.nickname}>'
