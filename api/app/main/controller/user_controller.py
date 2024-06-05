from app.auth_middleware import jwt_required
from flask_restx import Resource
from flask import request

from ..util.dto import user_dto
from ..service.user_service import user_service
from app.schema_middleware import expects_format
api = user_dto.api
user_id_schema = user_dto.user_id_schema
user_full_schema = user_dto.user_full_schema


@api.route('/', methods=['GET', 'PUT', 'POST', 'DELETE'])
class user_controller(Resource):
  
  @jwt_required
  @expects_format(user_id_schema)
  def get(self):
    """ Select single user by id """
    return user_service.get_by_id(request.json["id"])

  @jwt_required
  @expects_format(user_full_schema)
  def post(self):
    """ Create a new user """
    data = request.json   
    return user_service.create_user(data["username"], data["email"], data["passwd"], "USER")
  
  @jwt_required
  @expects_format(user_full_schema)
  def put(self):
    """ Modify user information """
    data = request.json
    return user_service.modify_user(data["id"], data["username"], data["email"], data["passwd"])
  
  @expects_format(user_id_schema)
  @jwt_required
  def delete(self):
     """ Delete a user by id"""
     return user_service.delete_by_id(request.json["id"])
        