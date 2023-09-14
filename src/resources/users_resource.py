from flask_restful import Resource
from flask import request
from src.repositories.user_repository import UserRepository
from src.schemas.user_schemas import UserSchema, UserDisplaySchema


class Users(Resource):

    def post(self):
        payload = UserSchema().load(request.json)
        response = UserRepository.insert_user(payload)
        response_schema = UserDisplaySchema()
        result = response_schema.dump(response)
        return result, 201