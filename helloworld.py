from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Greeting (Resource):
   def get(self):
      return { "message" : "Hello, world! Hi Flask, my old friend. It's good to talk with you again." }
api.add_resource(Greeting, '/') # Route_1

if __name__ == '__main__':
   app.run('0.0.0.0','8080')
