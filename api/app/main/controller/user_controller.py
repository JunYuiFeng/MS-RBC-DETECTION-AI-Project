from app.auth_middleware import jwt_required
from flask_restx import Resource
from flask import request

from ..util.dto import user_dto
from ..service.user_service import user_service
api = user_dto.api

@api.route('/')
class get_all(Resource):
  @jwt_required
  def get(self):
    """ select all users in the database """
    return user_service.get_all()
  
@api.route('/create')
class create_user(Resource):
  @jwt_required
  def post(self):
    """Create new user"""
    try:
      data = request.json
      if not data:
        return {
          "message": "Please provide user details",
          "data": None,
          "error": "Bad request"
        }, 400 # Bad request
      if not data["username"] or not data["email"] or not data["passwd"]:
        return {
          "message": "Incomplete data",
          "data": data,
          "error": "Bad request"
        }, 400 # bad request
          
      return user_service.create_user(data["username"], data["email"], data["passwd"])
    except Exception as e:
        return {
                "message": "Something went wrong!",
                "error": str(e),
                "data": None
        }, 500