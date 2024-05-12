from flask import Flask
from flask.app import Flask

def create_app() -> Flask:
  app = Flask(__name__)
  return app