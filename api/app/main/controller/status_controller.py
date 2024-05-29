from auth_middleware import jwt_required
from db import query_db
from flask import request
from flask_restx import Resource

from ..util.dto import status_dto

api = status_dto.api

@api.route('/')
class status_controller(Resource):
  @jwt_required
  def get(self):
    """ select all users in the database """
    posts = query_db("SELECT * FROM users")
    return posts