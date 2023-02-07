import os

# postgres_local_base = 'postgresql+psycopg2://{user}:{password}@{host}:{port}/{db_name}'.format(
#         user=os.environ.get('FLASK_DATABASE_USER', 'profit_sniper_api'),
#         password=os.environ.get('FLASK_DATABASE_PASSWORD', 'profit_sniper_api'),
#         host=os.environ.get('FLASK_DATABASE_HOST', '127.0.0.1'),
#         port=os.environ.get('FLASK_DATABASE_PORT', 5432),
#         db_name=os.environ.get('FLASK_DATABASE_NAME', 'profit_sniper_api'),
#     )
# postgres_local_base = os.environ['DATABASE_URL']

postgres_local_base='postgresql://postgres:blablabla@containers-us-west-23.railway.app:6794/railway' #troubled mist database

#get your connection string above. I am using railway

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'sirikali-sana-msee')
    DEBUG = False
    TOKEN_EXPIRE_HOURS = (24 * 365)

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = postgres_local_base
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = postgres_local_base
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = postgres_local_base


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

key = Config.SECRET_KEY
