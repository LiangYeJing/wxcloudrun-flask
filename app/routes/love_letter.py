from flask import Blueprint, request, jsonify
from app import db
from app.models.love_letter import LoveLetter
from app.models.user import User

love_letter_bp = Blueprint('love_letter', __name__)

@love_letter_bp.route('/send', methods=['POST'])
def send_love_letter():
    data = request.get_json()
    sender = User.query.get(data['sender_id'])
    receiver = User.query.get(data['receiver_id'])

    if sender and receiver:
        love_letter = LoveLetter(sender_id=sender.id, receiver_id=receiver.id, content=data['content'])
        db.session.add(love_letter)
        db.session.commit()
        return jsonify({"message": "Love letter sent successfully"}), 201
    return jsonify({"message": "User not found"}), 404
