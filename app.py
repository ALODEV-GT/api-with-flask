from flask import Flask, request
from flask_restful import Resource, Api

# Create reference of app
app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return {'message': 'Hello, World!'}


# Create the endpoints
api.add_resource(HelloWorld, '/api')

if __name__ == '__main__':
    # Start the Flask development web server.
    app.run(debug=True)
