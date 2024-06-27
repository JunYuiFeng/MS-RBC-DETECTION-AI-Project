import bcrypt
from db import query_db
from flask_restx import Resource
import logging
logging.basicConfig(level=logging.DEBUG)

class user_service(Resource):
  
  
  @staticmethod
  def get_all():
    users = query_db("SELECT id, username, email, role FROM users")
    return users
  
  @staticmethod
  def get_by_id(id: int):
    data = query_db("SELECT id, username, email, passwd FROM users WHERE id = ?", [id])
    return data
  
  @staticmethod
  def get_by_id_with_role(id: int):
    data = query_db("SELECT id, username, email, passwd, role FROM users WHERE id = ?", [id])
    return data
    
  @staticmethod
  def create_user(username: str, email: str, passwd: str, type):
    hashed_password = bcrypt.hashpw(passwd.encode('utf-8'), bcrypt.gensalt())
    res = query_db(
        "INSERT INTO users (username, email, passwd, role) VALUES (?, ?, ?, ?)",
        [username, email, hashed_password.decode('utf-8'), type],
        mod=True
    )
    return res
    
     
  @staticmethod
  def modify_user(id: int, username: str, email: str, passwd: str):
    if(passwd):
      hashed_password = bcrypt.hashpw(passwd.encode('utf-8'), bcrypt.gensalt())
      res = query_db("UPDATE users SET username = ?, email = ?, passwd = ? WHERE id = ?", [username, email, hashed_password.decode('utf-8'), id], mod=True)
    else:
      res = query_db("UPDATE users SET username = ?, email = ? WHERE id = ?", [username, email, id], mod=True)
    return res
    
  @staticmethod
  def delete_by_id(id: int):
    return query_db("DELETE FROM users WHERE id = ?", [id], mod=True)