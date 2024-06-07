import logging

from flask import jsonify
from flask_restx import Resource

from app.auth_middleware import jwt_required

logging.basicConfig(level=logging.DEBUG)
from ..service.user_service import user_service
from ..util.dto import users_dto

api = users_dto.api

@api.route('/')
class get_all(Resource):
  @jwt_required
  def get(self):
        """ Select all users in the database """
        try:
            users = user_service.get_all()
            logging.debug(f"Fetched users: {users}")
            return jsonify(users)
        except Exception as e:
            logging.error(f"Error fetching users: {e}")
            return {'message': 'An error occurred fetching users'}, 500
