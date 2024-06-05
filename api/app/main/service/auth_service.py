from typing import Dict, Tuple
from db import query_db
from flask_restx import Resource
from flask import current_app
import jwt

class auth_service(Resource):
  
  # can return boolean since query only returns 1 or 0
  @staticmethod
  def get_by_email_and_passwd(email: str, passwd: str):
    user_exists = query_db("SELECT EXISTS (SELECT 1 FROM users WHERE email = ? AND passwd = ?)", [email, passwd])
    user_exists = user_exists[0][0] # gets the  user_exists value  into 1 or 0
    return bool(user_exists)
  
  @staticmethod
  def login(email: str, passwd: str):
    data = query_db("SELECT id, username, email FROM users WHERE email = ? AND passwd = ?", [email, passwd], one=True)
    
    user = {
      "id": data[0],
      "username": data[1],
      "email": data[2]
    }
    
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
  
  
  @staticmethod
  def get_by_id(id: int):
    data = query_db("SELECT id, username, email FROM users WHERE id = ?", [id], one=True)
    return {
      "id": data[0],
      "username": data[1],
      "email": data[2]
    }