from flask_restx import Namespace, fields


class StatusDto:
    api = Namespace('status', description='status operations')
    user = api.model('status', {
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
        'public_id': fields.String(description='user Identifier')
    })