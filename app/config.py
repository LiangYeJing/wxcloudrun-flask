import os

class Config:
    """
    通用配置类
    """
    SECRET_KEY = os.environ.get('SECRET_KEY', 'default_secret_key')
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///default.db'

class DevelopmentConfig(Config):
    """
    开发环境配置类
    """
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:lyj52014@127.0.0.1:3306/flask_demo'

class ProductionConfig(Config):
    """
    生产环境配置类
    """
    SQLALCHEMY_DATABASE_URI = 'mysql://root:2yWHD4Pf@sh-cynosdbmysql-grp-1ri8v90y.sql.tencentcdb.com:23996/flask_demo'
    