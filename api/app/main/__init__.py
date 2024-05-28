import os

from flask import Flask
from flask.app import Flask

SECRET_KEY = os.environ.get('SECRET_KEY') or 'this is a secret'
def create_app() -> Flask:
  app = Flask(__name__)
  print(SECRET_KEY)
  app.config['SECRET_KEY'] = SECRET_KEY
  return app