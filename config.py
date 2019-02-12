import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://dunyung1:iamyung1@localhost/pitches'
    SECRET_KEY = os.environ.get('SECRET_KEY')
    UPLOADED_PHOTOS_DEST ='app/static/photos'

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True

#  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

config_options = {
'development':DevConfig,
'production':ProdConfig
}