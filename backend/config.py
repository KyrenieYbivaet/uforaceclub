import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', r'sqlite:///D:/progging/projects/uforaceclub/backend/instance/uforace.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key_here')
