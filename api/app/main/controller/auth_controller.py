from flask import request
from flask_restx import Resource
from typing import Dict, Tuple
import logging
from ..util.dto import auth_dto
from ..service.auth_service import auth_service
logging.basicConfig(level=logging.DEBUG)
api = auth_dto.api

@api.route('/')
class auth(Resource):
  @api.expect(auth_dto.user_schema)
  @api.doc(responses={
        200: ('Success', auth_dto.token_response),
        401: ('Unauthorized', auth_dto.error),
        500: ('Internal Server error', auth_dto.error)
  })
  def post(self) -> Tuple[int, Dict[str, str]]:
    """ login resource """
    data = request.json
    return auth_service.login(data["email"], data["passwd"])
  
