import os

class ProdConfig:
    pass

class DevConfig:
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}