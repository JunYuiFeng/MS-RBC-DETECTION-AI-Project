from app.auth_middleware import jwt_required
from flask_restx import Resource

from ..util.dto import status_dto

api = status_dto.api

@api.route('/')
class status_controller(Resource):
  @jwt_required
  def get(self):
    """ Returns string if app is running """
    return "We are online"