from flask import Blueprint, request, jsonify
from app import db
from app.models.image import Image
from app.models.couple import Couple

image_bp = Blueprint('image', __name__)

@image_bp.route('/upload', methods=['POST'])
def upload_image():
    data = request.get_json()
    couple = Couple.query.get(data['couple_id'])

    if couple:
        image = Image(couple_id=couple.id, image_url=data['image_url'])
        db.session.add(image)
        db.session.commit()
        return jsonify({"message": "Image uploaded successfully"}), 201
    return jsonify({"message": "Couple not found"}), 404
