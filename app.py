from flask import Blueprint
from flask_restful import Api
from flask_restful import Resource
from resources.Todo import TodoResource

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Route

api.add_resource(TodoResource, '/todo')
