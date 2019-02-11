import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://dunyung1:iamyung1@localhost/pitches'
    SECRET_KEY = os.environ.get('SECRET_KEY')


class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}