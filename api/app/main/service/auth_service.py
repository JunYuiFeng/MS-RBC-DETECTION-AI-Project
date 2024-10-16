from typing import Dict, Tuple

import bcrypt
from db import query_db
from flask_restx import Resource, marshal
from flask import current_app
import jwt
import datetime
from ..util.dto import auth_dto

class auth_service(Resource):
  
  # can return boolean since query only returns 1 or 0
  @staticmethod
  def get_by_email_and_passwd(email: str, passwd: str):
    user_exists = query_db("SELECT EXISTS (SELECT 1 FROM users WHERE email = ? AND passwd = ?)", [email, passwd], bool=True)
    return bool(user_exists)
  
  @staticmethod
  def login(email: str, passwd: str):
    res = query_db("SELECT id, username, email, passwd, role FROM users WHERE email = ?", [email])
    if res:
        res = res[0]
        # Compare the provided password with the hashed password
        if bcrypt.checkpw(passwd.encode('utf-8'), res['passwd'].encode('utf-8')):
            try:
                token = jwt.encode(
                    {"id": res['id'],
                     "username": res['username'],
                     'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1)  # Token expires in 1 day
                    },
                    current_app.config["SECRET_KEY"],
                    algorithm="HS256"
                )
                return marshal({
                    "message": "Successfully fetched authentication token",
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