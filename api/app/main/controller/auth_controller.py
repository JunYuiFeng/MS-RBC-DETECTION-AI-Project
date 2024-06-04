from flask import request
from flask_restx import Resource
from typing import Dict, Tuple

from ..util.dto import auth_dto
from ..service.auth_service import auth_service
from app.schema_middleware import expects_format

api = auth_dto.api
login_schema = auth_dto.user_schema

@api.route('/')
class auth(Resource):
  @expects_format(login_schema)
  def post(self) -> Tuple[int, Dict[str, str]]:
    """ login resource """
    data = request.json
    #validate input
    validated = auth_service.get_by_email_and_passwd(data["email"], data["passwd"])
    if validated is not True:
      return {
        "message": "Invalid data",
        "data": None,
        "error": validated
      }
    return auth_service.login(data["email"], data["passwd"])
  
