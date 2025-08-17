from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# 初始化数据库
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    # 配置选择
    app.config.from_object('app.config.DevelopmentConfig')

    # 初始化数据库和迁移工具
    db.init_app(app)
    migrate.init_app(app, db)

    # 在应用实例化后再注册蓝图
    from app.routes.auth import auth_bp
    from app.routes.couple import couple_bp
    from app.routes.image import image_bp
    from app.routes.love_letter import love_letter_bp

    # 注册蓝图
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(couple_bp, url_prefix='/couple')
    app.register_blueprint(image_bp, url_prefix='/image')
    app.register_blueprint(love_letter_bp, url_prefix='/love_letter')

    return app
