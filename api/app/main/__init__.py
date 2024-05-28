import os

from flask import Flask
from db import init_db


SECRET_KEY = os.environ.get('SECRET_KEY') or 'this is a secret'
def create_app() -> Flask:
  app = Flask(__name__)
  app.config['SECRET_KEY'] = SECRET_KEY
  with app.app_context():
    init_db()
    
  return app