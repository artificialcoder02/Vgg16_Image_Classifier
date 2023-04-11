import os
from flask import Flask
from config import Config

class Config:
    SECRET_KEY = os.environ.get('password') or 'password'
    # Define the path to your pre-trained model
    MODEL_PATH = 'cats_and_dogs\cats_and_dogs\model_vgg16.h5'
    # Define the allowed file extensions for image uploads
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
    # Define the maximum file size for image uploads (in bytes)
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16 MB


