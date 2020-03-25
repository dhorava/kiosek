import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    DB_API_KEY = os.environ.get('DB_API_KEY') or 'dapi76a91a2c9fc7bc4c99f2d4e24d7bd18e'
    UPLOAD_FOLDER = '/static/uploads'
    ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'csv', 'xlsx'}
