from functools import wraps
from .main.service.user_service import user_service
import jwt
import base64
from flask import current_app, request


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
      jwt_data = jwt.decode(token, current_app.config["SECRET_KEY"], algorithms=["HS256"])
      current_user = user_service.get_by_id(jwt_data["id"])
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
    return f(*args, **kwargs)
  return decorated