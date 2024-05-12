import os
from app import blueprint
from app.main import create_app
from flask import request, jsonify

dummy_keys = {'api_key1': 'user1', 'api_key2': 'user2'}


app = create_app()
app.register_blueprint(blueprint)
app.app_context().push()


def authenticate_api_key(api_key):
  return dummy_keys.get(api_key)

@app.before_request
def before_request():
  api_key = request.headers.get('API-key')
  if not api_key or not authenticate_api_key(api_key):
    return jsonify({'error': 'Unauthorized'}), 401

