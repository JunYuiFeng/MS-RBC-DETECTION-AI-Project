from flask import request
from flask_restx import Resource
from typing import Dict, Tuple
import logging
from ..util.dto import auth_dto
from ..service.auth_service import auth_service
logging.basicConfig(level=logging.DEBUG)
api = auth_dto.api
login_schema = auth_dto.user_schema

@api.route('/')
class auth(Resource):

  @api.expect(auth_dto.user_schema)
  @api.marshal_with(auth_dto.token_response)
  def post(self) -> Tuple[int, Dict[str, str]]:
    """ login resource """
    data = request.json
    #validate input
    validated = auth_service.get_by_email_and_passwd(data["email"], data["passwd"])
    if not validated:
      return {
        "message": "Invalid credentials",
        "data": None,
        "error": validated
      }, 401
    return auth_service.login(data["email"], data["passwd"])
  
