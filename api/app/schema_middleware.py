from functools import wraps
from flask import request
from jsonschema import validate, FormatChecker, ValidationError, validators
from jsonschema.validators import _LATEST_VERSION as LATEST_VALIDATOR
from typing import Iterable



def validate_json(f):
  @wraps(f)
  def wrapper(*args, **kwargs):
    try:
      request.json
    except Exception as e:
      return {
          "message": "Payload must be a valid json",
          "data": None,
          "error": "Bad request"
        }, 400 # Bad request
    return f(*args, **kwargs)
  return wrapper


def expects_format(schema=None, check_formats=False):
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
        
      format_checker = None
        
      if check_formats:
        if isinstance(check_formats, Iterable):
          format_checker = FormatChecker(check_formats)
        elif isinstance(check_formats, bool):
          format_checker = FormatChecker()
        else:
          return {
            "message": "check_formats must be bool or iterable",
            "data": None,
            "error": "Bad request"
          }, 400 # Bad request

      try:
        validate(data, schema, format_checker=format_checker)
      except ValidationError as e:
        return {
                "message": "Validation error",
                "error": str(e),
                "data": None
        }, 400
      return f(*args, **kwargs)
    return decorator_func
  return decorator
  
