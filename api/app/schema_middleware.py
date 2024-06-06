from functools import wraps
from flask import request
from jsonschema import validate, ValidationError


def expects_format(schema=None):
  if schema is None:
    schema = dict()
  
  def decorator(f):
    @wraps(f)
    def decorator_func(*args, **kwargs):
      try:
        data = request.json
      except Exception as e:
        return {
            "message": "Payload must be a valid json",
            "data": None,
            "error": "Bad request"
          }, 400 # Bad request
        
      try:
        validate(data, schema)
      except ValidationError as e:
        return {
                "message": "Validation error",
                "error": str(e),
                "data": None
        }, 400
      return f(*args, **kwargs)
    return decorator_func
  return decorator
  
