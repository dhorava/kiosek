import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):

    # databricks
    DB_API_KEY = 'dapi76a91a2c9fc7bc4c99f2d4e24d7bd18e'


    # blob storage

    REDMEDIADWH_KEY = 'ePYDdZb74+ZxX1Ij/Ue+nMyMGQePX8fXVyxsllcR3OtEoYneLmnzjAOQC4sxonFCtLhDT3VyCZ9mDhxSQ7aWzw=='

    # mssql

    MSSQL_USERNAME = 'roiblock@roiblock'
    MSSQL_PWD = '9a5obZQU'

    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://roiblock@roiblock:9a5obZQU@roiblock.database.windows.net:1433/Campaigns' # [DB_TYPE]+[DB_CONNECTOR]://[USERNAME]:[PASSWORD]@[HOST]:[PORT]/[DB_NAME]
    SQLALCHEMY_ECHO = True # Flask-SQLAlchemy will log all database activity to Python's stderr for debugging purposes
    SQLALCHEMY_TRACK_MODIFICATIONS = False # signal the application every time a change is about to be made in the database


    # misc

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    UPLOAD_FOLDER = '/static/uploads'
    ALLOWED_EXTENSIONS = {'xls', 'xlsx'}
