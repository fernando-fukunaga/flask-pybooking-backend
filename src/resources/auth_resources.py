from flask_restful import Resource
from flask import request
from src.repositories.user_repository import UserRepository
from src.schemas import user_schemas
from src.utils.auth_utils import get_logged_in_user, verify_headers_and_retrieve_token

repository = UserRepository()


class AuthSignUp(Resource):

    def post(self):
        payload = user_schemas.User().load(request.json)
        response_model = user_schemas.UserNoPassword()
        response = response_model.dump(repository.insert_user(payload))
        return response, 201
    

class AuthSignIn(Resource):

    def post(self):
        payload = user_schemas.SignIn().load(request.json)
        response = repository.sign_in_user(payload)
        return response, 200
    

class AuthMe(Resource):

    def get(self):
        response_model = user_schemas.UserNoPassword()
        token = verify_headers_and_retrieve_token(request)
        response = response_model.dump(get_logged_in_user(token))
        return response, 200
