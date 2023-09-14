from flask import Flask
from flask_restful import Api
from src.resources.users_resource import Users

app = Flask(__name__)
api = Api(app)
api.add_resource(Users, "/users/signup")

if __name__ == "__main__":
    app.run()
