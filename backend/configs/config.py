from dotenv import load_dotenv  # type: ignore
import os

load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    if not SQLALCHEMY_DATABASE_URI:
        raise ValueError("DATABASE_URL environment variable is not set.")

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    JWT_SECRET = os.getenv('JWT_SECRET')
    if not JWT_SECRET:
        raise ValueError("JWT_SECRET environment variable is not set.")
    
    JWT_EXPIRATION = int(os.getenv('JWT_EXPIRATION', 3600))  # Default to 1 hour
    JWT_BLACKLIST_ENABLED = True
    JWT_BLACKLIST_TOKEN_CHECKS = ['access', 'refresh']

    ENV = os.getenv('ENV', 'development')  # Default to 'development'
