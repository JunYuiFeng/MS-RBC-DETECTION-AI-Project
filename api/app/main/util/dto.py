from flask_restx import Namespace, fields


class status_dto:
    api = Namespace('status', description='status operations')
    user = api.model('status', {
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
    })
    
    
class auth_dto:
    api = Namespace('auth', description='authentication operations')
    user = api.model('auth', {
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
    })    
    
class users_dto:
    api = Namespace('users', description='user-crud operations')
    
class user_dto:
    api = Namespace('user', description='single user operations')