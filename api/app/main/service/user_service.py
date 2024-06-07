from db import query_db
from flask_restx import Resource


class user_service(Resource):
  
  @staticmethod
  def get_all():
    users = query_db("SELECT id, username, email, passwd, role FROM users")
    return users;
  
  @staticmethod
  def get_by_id(id: int):
    data = query_db("SELECT id, username, email, passwd, role FROM users WHERE id = ?", [id])
    return data
    
  @staticmethod
  def create_user(username: str, email: str, passwd: str, type):
    return query_db("INSERT INTO users (username, email, passwd, role ) VALUES (?, ?, ?, ?)", [username, email, passwd, type], mod=True)
     
  @staticmethod
  def modify_user(id: int, username: str, email: str, passwd: str):
    return query_db("UPDATE users SET username = ?, email = ?, passwd = ? WHERE id = ?", [username, email, passwd, id], mod=True)
    
  @staticmethod
  def delete_by_id(id: int):
    return query_db("DELETE FROM users WHERE id = ?", [id], mod=True)