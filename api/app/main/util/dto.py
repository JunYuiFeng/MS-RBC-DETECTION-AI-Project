from flask_restx import Namespace, fields


class status_dto:
    api = Namespace('status', description='status operations')
    
    
class auth_dto:
    api = Namespace('auth', description='authentication operations')
    user_schema = {
        'type': 'object',
        'properties': {
            'email': {'type': 'string'},
            'passwd': {'type': 'string'}
        },
        'required': ['email', 'passwd']
    }
    
class users_dto:
    api = Namespace('users', description='user-crud operations')
    
class user_dto:
    api = Namespace('user', description='single user operations')
    user_get_schema = {
        'type': 'object',
        'properties': {
            'id': {'type': 'integer'},
        },
        'required': ['id']
    }