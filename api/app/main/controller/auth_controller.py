import jwt
from flask import request, current_app
from flask_restx import Resource
from typing import Dict, Tuple

from ..util.dto import auth_dto
from ..service.auth_service import auth_service

api = auth_dto.api

@api.route('/')
class auth(Resource):
  
  def post() -> Tuple[int, Dict[str, str]]:
    """ login resource """
    try:
      data = request.json
      if not data:
        return {
          "message": "Please provide user details",
          "data": None,
          "error": "Bad request"
        }, 400 # Bad request
        
      #validate input
      validated = auth_service.get_by_email_and_passwd(data["email"], data["passwd"])
      if validated is not True:
        return {
          "message": "Invalid data",
          "data": None,
          "error": validated
        }
      user = auth_service.login(data["email"], data["passwd"])
      
      if user:
            try:
              user["token"] = jwt.encode(
                {"id": user["id"]}, 
                current_app.config["SECRET_KEY"], 
                algorithm="HS256")
              return {
                "message": "succesfully fetched authentication token",
                "data": user
              }, 200
            except Exception as e:
              return {
                "message": "Something went wrong",
                "data": None,
                "error": str(e)
              }, 500
      return {
          "message": "Error fetching auth token!, invalid email or password",
          "data": None,
          "error": "Unauthorized"
        }, 404
    except Exception as e:
        return {
                "message": "Something went wrong!",
                "error": str(e),
                "data": None
        }, 500
  
