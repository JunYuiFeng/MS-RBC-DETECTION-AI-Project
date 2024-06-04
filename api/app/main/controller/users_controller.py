from app.auth_middleware import jwt_required
from flask_restx import Resource
from flask import request

from ..util.dto import users_dto
from ..service.user_service import user_service
api = users_dto.api

# TODO: Rewrite code to allow for get/update/delete on 1 enpoint
@api.route('/')
class get_all(Resource):
  @jwt_required
  def get(self):
    """ select all users in the database """
    return user_service.get_all()