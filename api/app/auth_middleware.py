from functools import wraps
from .main.service.auth_service import auth_service
import jwt
import base64
from flask import abort, current_app, request




## apply @jwt_required to secure endpoints
def jwt_required(f):
  @wraps(f)
  def decorated(*args, **kwargs):
    token = None
    if "Authorization" in request.headers:
      token = request.headers["Authorization"].split(" ")[1]
    if not token:
      return {
        "message": "No Authentication token provided",
        "data": None,
        "error": "Unauthorized"
      }, 401 # Unauthorized
    try: 
      # if token:
      #   return f(*args, **kwargs)
      # return decorated
      jwt_data = jwt.decode(token, current_app.config["SECRET_KEY"], algorithms=["HS256"])
      # current_user= None ## implement get user by id
      current_user = auth_service.get_user_by_id(jwt_data["id"])
      if current_user is None:
        return {
          "message": "Invalid Authentication token provided",
          "data": None,
          "error": "Unauthorized"
        }, 401 # Unauthorized
    except Exception as e:
      return {
        "message": "Server error",
        "data": None,
        "error": str(e)
      }, 500 # server error
    return f(current_user, *args, **kwargs)
  return decorated