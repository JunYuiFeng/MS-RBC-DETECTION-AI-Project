from functools import wraps

import jwt
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
      current_user= None ## implement get user by id
      if current_user is None:
        return {
          "message": "Invalid Authentication token provided",
          "data": None,
          "error": "Unauthorized"
        }, 401 # Unauthorized
      if not current_user["active"]:
        abort(403)
    except Exception as e:
      return {
        "message": "Server error",
        "data": None,
        "error": str(e)
      }, 500 # server error
    return f(current_user, *args, **kwargs)
  return decorated


def deco(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        print("decorated")
        return f(*args, **kwargs)
    return decorated_function   
        