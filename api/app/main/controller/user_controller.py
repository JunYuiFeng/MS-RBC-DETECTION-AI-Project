from app.auth_middleware import jwt_required
from flask_restx import Resource
from flask import request

from ..util.dto import user_dto
from ..service.user_service import user_service
api = user_dto.api

# TODO: Rewrite code to allow for get/update/delete on 1 enpoint
@api.route('/', methods=['POST', 'GET', 'DELETE'])
class get_all(Resource):
  @jwt_required
  def get(self):
    """ Select single user by id """
    return user_service.get_all()
  
  @jwt_required
  def post(self):
    """ Create a new user """
    return create_user()
  
  @jwt_required
  def delete(self):
     """ Delete a user by id"""
     return delete_user()


def create_user():
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
  
def delete_user():
    try:
      data = request.json
      if not data:
        return {
          "message": "Please provide user details",
          "data": None,
          "error": "Bad request"
        }, 400 # Bad request
      if not data["id"]:
        return {
          "message": "Incomplete data",
          "data": data,
          "error": "Bad request"
        }, 400 # bad request
          
      return user_service.delete_by_id(data["id"])
    except Exception as e:
        return {
                "message": "Something went wrong!",
                "error": str(e),
                "data": None
        }, 500
        