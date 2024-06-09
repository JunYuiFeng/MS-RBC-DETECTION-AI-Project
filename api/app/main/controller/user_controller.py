from app.auth_middleware import jwt_required
from flask import request
from flask_restx import Resource

from ..service.user_service import user_service
from ..util.dto import user_dto

api = user_dto.api


@api.route('/', methods=['GET', 'PUT', 'POST', 'DELETE'])
class user_controller(Resource):

    @jwt_required()
    @api.expect(user_dto.user_id_schema)
    @api.marshal_with(user_dto.user_full_schema, skip_none=True)
    @api.doc(responses={
          401: ('Unauthorized', user_dto.error),
          500: ('Internal Server error', user_dto.error)
    })
    def get(self):
        """ Select single user by id """
        return user_service.get_by_id(request.json["id"])

    @jwt_required(role="ADMIN")
    @api.expect(user_dto.user_create_schema)
    @api.doc(responses={
          200: 'Succes',
          401: ('Unauthorized', user_dto.error),
          500: ('Internal Server error', user_dto.error)
    })
    def post(self):
        """ Create a new user """
        data = request.json
        return user_service.create_user(data["username"], data["email"], data["passwd"], "USER")

    @jwt_required(role="ADMIN")
    @api.expect(user_dto.user_mod_schema)
    @api.marshal_with(user_dto.user_full_schema)
    @api.doc(responses={
          401: ('Unauthorized', user_dto.error),
          500: ('Internal Server error', user_dto.error)
    })
    def put(self):
        """ Modify user information """
        data = request.json
        return user_service.modify_user(data["id"], data["username"], data["email"], data["passwd"])

    @jwt_required(role="ADMIN")
    @api.expect(user_dto.user_id_schema)
    @api.doc(responses={
          200: 'Success',
          401: ('Unauthorized', user_dto.error),
          500: ('Internal Server error', user_dto.error)
    })
    def delete(self):
        """ Delete a user by id"""
        return user_service.delete_by_id(request.json["id"])
