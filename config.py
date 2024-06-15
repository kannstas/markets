import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://postgres:19691970@localhost:5431/farmers_markets'
    SQLALCHEMY_TRACK_MODIFICATIONS = False