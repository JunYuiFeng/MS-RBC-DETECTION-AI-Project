from db import query_db
from flask_restx import Resource

class user_service(Resource):
  
  @staticmethod
  def get_all():
    users = query_db("SELECT id, username, email, passwd, role FROM users")
    return users;
  
  # can return boolean since query only returns 1 or 0
  @staticmethod
  def get_by_email_and_passwd(email: str, passwd: str):
    user_exists = query_db("SELECT EXISTS (SELECT 1 FROM users WHERE email = ? AND passwd = ?)", [email, passwd])
    return bool(user_exists)
  
  @staticmethod
  def get_by_id(id: int):
    data = query_db("SELECT id, username, email, passwd, role  FROM users WHERE id = ?", [id], one=True)
    return {
      "id": data[0],
      "username": data[1],
      "email": data[2]
    }
     
  @staticmethod
  def create_user(username: str, email: str, passwd: str, type):
    return query_db("INSERT INTO users (username, email, passwd, rolepi ) VALUES (?, ?, ?, ?)", [username, email, passwd, type], mod=True)
    
  @staticmethod
  def delete_by_id(id: int):
    return query_db("DELETE FROM users WHERE id = ?", [id], mod=True)