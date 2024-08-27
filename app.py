from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


class GettingStarted(Resource):
    def get(self):
        return {"data" : "HIII"}

api.add_resource(GettingStarted, "/hello")


if __name__ == "__main__":
    app.run(debug=True)

