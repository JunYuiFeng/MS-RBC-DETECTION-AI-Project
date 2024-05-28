from flask import request
from flask_restx import Resource
from auth_middleware import jwt_required

from ..util.dto import StatusDto

api = StatusDto.api

@api.route('/')
class StatusList(Resource):
  @jwt_required
  def get(self):
    return 'Hello, World!'