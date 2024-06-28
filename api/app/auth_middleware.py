from functools import wraps
from .main.service.user_service import user_service
import jwt
import base64
from flask import current_app, request


def jwt_required(role=None):

    def decorator(f):

        @wraps(f)
        def decorated(*args, **kwargs):
            token = None
            current_user = None

            # Check for token in Authorization header
            if "Authorization" in request.headers:
                auth_header = request.headers["Authorization"].split()
                if len(auth_header) == 2 and auth_header[0] == "Bearer":
                    token = auth_header[1]

            if not token:
                return {
                    "message": "No Authentication token provided",
                    "data": None,
                    "error": "Unauthorized"
                }, 401  # Unauthorized

            try:
                # Decode the JWT token
                jwt_data = jwt.decode(token,
                                      current_app.config["SECRET_KEY"],
                                      algorithms=["HS256"])
                current_user = user_service.get_by_id_with_role(jwt_data["id"])

                # no user
                if current_user is None:
                    return {
                        "message": "Invalid Authentication token provided",
                        "data": None,
                        "error": "Unauthorized"
                    }, 401  # Unauthorized

                if 'exp' not in jwt_data:
                    return {
                        "message": "No expiry date in token",
                        "data": None,
                        "error": "Unauthorized"
                    }, 401  # Unauthorized

                user_role = current_user[0]['role']
                if role and user_role not in [role, "ADMIN"]:
                    return {
                        "message": "Insufficient permissions",
                        "data": None,
                        "error": "Forbidden"
                    }, 403  # Forbidden

            except jwt.ExpiredSignatureError:
                return {
                    "message": "Token expired",
                    "data": None,
                    "error": "Unauthorized"
                }, 401  # Unauthorized

            except jwt.InvalidTokenError as e:
                return {
                    "message": "Invalid token",
                    "data": None,
                    "error": str(e)
                }, 401  # Unauthorized

            except Exception as e:
                return {
                    "message": "Server error",
                    "data": current_user,
                    "error": str(e)
                }, 500  # Server error
            return f(*args, **kwargs)
        return decorated
    return decorator
