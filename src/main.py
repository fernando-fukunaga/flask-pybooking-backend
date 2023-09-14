from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

table_hotels = {}

parser = reqparse.RequestParser()
parser.add_argument("hotel_name", type=str)


class Hotels(Resource):

    def post(self):
        args = parser.parse_args()
        table_hotels['1'] = {"name": args["hotel_name"]}

    def get(self):
        return table_hotels


api.add_resource(Hotels, "/hotels")

if __name__ == "__main__":
    app.run(debug=True)
