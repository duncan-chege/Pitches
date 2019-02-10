import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://dunyung1:iamyung1@localhost/watchlist'

class ProdConfig:
    pass

class DevConfig:
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}