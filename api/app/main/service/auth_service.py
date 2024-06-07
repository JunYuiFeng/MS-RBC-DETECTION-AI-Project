from typing import Dict, Tuple
from db import query_db
from flask_restx import Resource
from flask import current_app
import jwt

class auth_service(Resource):
  
  # can return boolean since query only returns 1 or 0
  @staticmethod
  def get_by_email_and_passwd(email: str, passwd: str):
    user_exists = query_db("SELECT EXISTS (SELECT 1 FROM users WHERE email = ? AND passwd = ?)", [email, passwd], bool=True)
    return bool(user_exists)
  
  @staticmethod
  def login(email: str, passwd: str):
    res = query_db("SELECT id, username, email, passwd, role FROM users WHERE email = ? AND passwd = ?", [email, passwd])[0]
    if res:
            try:
              token = jwt.encode(
                {"id": res['id']}, 
                current_app.config["SECRET_KEY"], 
                algorithm="HS256")
              return {
                "message": "succesfully fetched authentication token",
                "data": {
                  "user": res,
                  "token": token
                }
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
  
  
  @staticmethod
  def get_by_id(id: int):
    data = query_db("SELECT id, username, email FROM users WHERE id = ?", [id])
    return {
      "id": data[0],
      "username": data[1],
      "email": data[2]
    }