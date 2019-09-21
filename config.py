import os

class Config:
    # SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    SECRET_KEY = os.environ.get('SECRET_KEY')
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    # QLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://wecode:New@localhost/pitches'
class ProdConfig(Config):
    # SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    QLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://wecode:News@localhost/pitches'

class DevConfig(Config):
    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig
}