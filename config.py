import os


basedir = os.path.abspath(os.path.dirname(__file__))
#
# SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
# SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')



class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True