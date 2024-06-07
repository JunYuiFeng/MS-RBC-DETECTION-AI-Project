from flask import Flask
from db import init_db
from flask_cors import CORS


SECRET_KEY = 'DefaultSigningKey'
def create_app() -> Flask:
  app = Flask(__name__)
  app.config['SECRET_KEY'] = SECRET_KEY
  with app.app_context():
    init_db()
    
  CORS(app)
 
  return app