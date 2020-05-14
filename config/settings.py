import os

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                          'postgresql://username:password@hostname/database'
APP_NAME = os.environ.get('APP_NAME')
SERVER_NAME = os.environ.get('SERVER_NAME')
DEBUG = os.environ.get('DEBUG') or False
PORT = os.environ.get('PORT')
