from flask import Blueprint, request, jsonify
from app import db
from app.models.couple import Couple
from app.models.user import User

couple_bp = Blueprint('couple', __name__)

@couple_bp.route('/bind', methods=['POST'])
def bind_couple():
    data = request.get_json()
    user1 = User.query.get(data['user1_id'])
    user2 = User.query.get(data['user2_id'])

    if user1 and user2:
        couple = Couple(user1_id=user1.id, user2_id=user2.id)
        db.session.add(couple)
        db.session.commit()
        return jsonify({"message": "Couple bound successfully"}), 201
    return jsonify({"message": "User not found"}), 404
