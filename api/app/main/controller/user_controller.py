from app.auth_middleware import jwt_required
from flask_restx import Resource, fields
from flask import request


from ..util.dto import user_dto
from ..service.user_service import user_service
api = user_dto.api


@api.route('/', methods=['GET', 'PUT', 'POST', 'DELETE'])
class user_controller(Resource):
  
  @api.expect(user_dto.user_id_schema)
  @api.marshal_with(user_dto.user_full_schema, skip_none=True)
  @jwt_required
  def get(self):
    """ Select single user by id """
    return user_service.get_by_id(request.json["id"])

  @api.expect(user_dto.user_mod_schema)
  @jwt_required
  def post(self):
    """ Create a new user """
    data = request.json   
    return user_service.create_user(data["username"], data["email"], data["passwd"], "USER")
  
  
  @api.expect(user_dto.user_mod_schema)
  @api.marshal_with(user_dto.user_full_schema)
  @jwt_required
  def put(self):
    """ Modify user information """
    data = request.json
    return user_service.modify_user(data["id"], data["username"], data["email"], data["passwd"])
  
  @api.expect(user_dto.user_id_schema)
  @jwt_required
  def delete(self):
     """ Delete a user by id"""
     return user_service.delete_by_id(request.json["id"])
        