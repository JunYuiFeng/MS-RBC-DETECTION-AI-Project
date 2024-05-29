from typing import Dict, Tuple
from db import query_db
from flask_restx import Resource

class auth_service(Resource):
  
  # can return boolean since query only returns 1 or 0
  @staticmethod
  def get_by_email_and_passwd(email: str, passwd: str):
    user_exists = query_db("SELECT EXISTS (SELECT 1 FROM users WHERE email = ? AND passwd = ?)", [email, passwd])
    return bool(user_exists)
  
  @staticmethod
  def login(email: str, passwd: str):
    data = query_db("SELECT id, username, email FROM users WHERE email = ? AND passwd = ?", [email, passwd], one=True)
    return {
      "id": data[0],
      "username": data[1],
      "email": data[2]
    }
  
  @staticmethod
  def get_by_id(id: int):
    data = query_db("SELECT id, username, email FROM users WHERE id = ?", [id], one=True)
    return {
      "id": data[0],
      "username": data[1],
      "email": data[2]
    }