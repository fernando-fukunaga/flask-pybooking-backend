from flask_restful import Resource
from flask import request
from src.services import user_services
from src.schemas import user_schemas
from src.utils.auth_utils import get_logged_in_user, verify_headers_and_retrieve_token


class AuthSignUp(Resource):

    def post(self):
        payload = user_schemas.User().load(request.json)
        response = user_services.sign_up_service(payload)
        return response, 201
    

class AuthSignIn(Resource):

    def post(self):
        payload = user_schemas.SignIn().load(request.json)
        response = user_services.sign_in_service(payload)
        return response, 200


class AuthMe(Resource):

    def get(self):
        response_model = user_schemas.UserNoPassword()
        token = verify_headers_and_retrieve_token(request)
        response = response_model.dump(get_logged_in_user(token))
        return response, 200
