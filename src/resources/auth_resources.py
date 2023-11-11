from flask_restful import Resource, reqparse
from flask import request
from werkzeug.exceptions import Unauthorized
from src.repositories.user_repository import UserRepository
from src.schemas import user_schemas
from src.utils.current_user import current_user
from src.utils.auth_utils import token_is_valid

repository = UserRepository()
parser = reqparse.RequestParser()


class AuthSignUp(Resource):

    def post(self):
        payload = user_schemas.User().load(request.json)
        response_model = user_schemas.UserNoPassword()
        response = response_model.dump(repository.insert_user(payload))
        return response, 201
    

class AuthSignIn(Resource):

    def post(self):
        payload = user_schemas.SignIn().load(request.json)
        response_model = user_schemas.SucessfulSignIn()
        response = response_model.dump(repository.authenticate_user(payload))
        return response, 200
    

class AuthMe(Resource):

    def get(self):
        response_model = user_schemas.UserNoPassword()
        token = parser.add_argument('Authorization', location='headers')
        if token_is_valid(token):
            response = response_model.dump(repository.get_user_by_email(current_user.email))
            return response, 200
        else:
            raise Unauthorized(description="Invalid bearer token!")
