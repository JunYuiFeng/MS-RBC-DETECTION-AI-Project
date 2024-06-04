from flask_restx import Namespace, fields


class status_dto:
    api = Namespace('status', description='status operations')
    
    
class auth_dto:
    api = Namespace('auth', description='authentication operations')
    user_schema = {
        "email": "string",
        "passwd": "string"
    }  
    
class users_dto:
    api = Namespace('users', description='user-crud operations')
    
class user_dto:
    api = Namespace('user', description='single user operations')
    user_get_schema = {
        'id': 'integer'
    }