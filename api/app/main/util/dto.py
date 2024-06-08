from flask_restx import Namespace
from flask_restx import fields
from werkzeug.datastructures import FileStorage


error = {
    'message': fields.String,
    'data': fields.String,
    'error': fields.String
 }

class user_dto:
    api = Namespace('user', description='single user operations')
    user_id_schema = api.model('input_id_requests', {'id': fields.Integer});
    
    common = {
        'id': fields.Integer(required=True, description='ID cannot be blank'),
        'username': fields.String(required=True, description='usename cannot be blank on insertion of a new user'),
        'email': fields.String(required=True, description='email cannot be blank on insertion of a new user'),
        'passwd': fields.String(required=True, description='password cannot be blank on insertion of a new user'),
    }
    
    user_mod_schema =  api.model('user_mod', common) 
    user_full_schema =  api.model('user', {
        **common,
        'role': fields.String(required=False, description='role of user cannot be assigned when creating a user')
    }) 
    error = api.model('error', {**error})
    
class auth_dto:
    api = Namespace('auth', description='authentication operations')
    user_schema = api.model('user_login', {
        'email': fields.String(required=True, description='email cannot be blank on request for token'),
        'passwd': fields.String(required=True, description='password cannot be blank on request for token'),
    })
    
    token_response = api.model('token_response', {
        'message': fields.String,
        'data': fields.Nested(api.model('data', {
            'user': fields.Nested(user_dto.user_full_schema),
            'token': fields.String
        }))
    })
    error = api.model('error', {**error})
    
class users_dto:
    api = Namespace('users', description='user-crud operations')
    users_schema = api.model('users_list', {
        'users': fields.List(fields.Nested(user_dto.user_full_schema))
    })

class predict_dto:
    api = Namespace('predict', description='Prediction operations')
    
    parser = api.parser()
    parser.add_argument('image', location='files', type=FileStorage, required=True, help='Image')
    predict_data = api.model('predict_data', {
        'deformedCellsDetected': fields.Integer,
        'healthyCellsDetected': fields.Integer,
        'annotatedImage': fields.String
    })
    