from flask import request
from flask_restx import Resource

from ..util.dto import StatusDto

api = StatusDto.api

@api.route('/')
class StatusList(Resource):
  def get(self):
    return 'Hello, World!'