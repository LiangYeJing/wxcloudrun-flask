from flask import Blueprint, request, jsonify
from app import db
from app.models.user import User

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    # 检查用户是否已经存在
    user = User.query.filter_by(openid=data['openid']).first()

    if user:
        # 用户已存在，返回用户信息
        return jsonify({
            "message": "User logged in successfully",
            "user": {
                "id": user.id,
                "openid": user.openid,
                "nickname": user.nickname,
                "avatar_url": user.avatar_url,
                "created_at": user.created_at
            }
        }), 200
    else:
        # 用户不存在，进行注册
        user = User(
            openid=data['openid'],
            nickname=data['nickname'],
            avatar_url=data['avatar_url']
        )
        db.session.add(user)
        db.session.commit()
        
        return jsonify({
            "message": "User registered successfully",
            "user": {
                "id": user.id,
                "openid": user.openid,
                "nickname": user.nickname,
                "avatar_url": user.avatar_url,
                "created_at": user.created_at
            }
        }), 201
