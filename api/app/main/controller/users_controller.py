from app.auth_middleware import jwt_required
from flask_restx import Resource

from ..util.dto import users_dto
from ..service.user_service import user_service
api = users_dto.api

@api.route('/')
class get_all(Resource):
  @jwt_required
  def get(self):
    """ select all users in the database """
    return user_service.get_all()