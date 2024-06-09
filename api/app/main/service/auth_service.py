from typing import Dict, Tuple
from db import query_db
from flask_restx import Resource, marshal
from flask import current_app
import jwt
from ..util.dto import auth_dto

class auth_service(Resource):
  
  # can return boolean since query only returns 1 or 0
  @staticmethod
  def get_by_email_and_passwd(email: str, passwd: str):
    user_exists = query_db("SELECT EXISTS (SELECT 1 FROM users WHERE email = ? AND passwd = ?)", [email, passwd], bool=True)
    return bool(user_exists)
  
  @staticmethod
  def login(email: str, passwd: str):
    res = query_db("SELECT id, username, email, passwd, role FROM users WHERE email = ? AND passwd = ?", [email, passwd])
    if res:
            try:
              res = res[0]
              token = jwt.encode(
                {"id": res['id']}, 
                current_app.config["SECRET_KEY"], 
                algorithm="HS256")
              return marshal({
                "message": "succesfully fetched authentication token",
                "data": {
                  "user": res,
                  "token": token
                }
              }, auth_dto.token_response), 200
            except Exception as e:
              return {
                "message": "Something went wrong",
                "data": None,
                "error": str(e)
              }, 500
    return marshal({
        "message": "Invalid email or password",
        "data": None,
        "error": "Unauthorized"
      }, auth_dto.error), 401