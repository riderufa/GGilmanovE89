import os

class Configuration(object):
    DEBUG = True
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:docker@172.19.0.2/test'
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY')
    # SECRET_KEY = 'kajsdkjasfasdkfjahsdkjh'
    CELERY_BROKER_URL=os.getenv('CELERY_BROKER_URL')
    # CELERY_BROKER_URL='redis://172.19.0.4'
    CELERY_RESULT_BACKEND=os.getenv('CELERY_RESULT_BACKEND')
    # CELERY_RESULT_BACKEND='redis://172.19.0.4'
    NSQD_SERVER=os.getenv('NSQD_SERVER')
    # NSQD_SERVER='172.19.0.6:4151'
    # CELERY_IMPORTS = ['app', 'view']

