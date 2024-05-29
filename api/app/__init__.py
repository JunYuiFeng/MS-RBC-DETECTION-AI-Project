from flask import Blueprint
from flask_restx import Api

from .main.controller.status_controller import api as status_ns
from .main.controller.predict_controller import predict_ns
from .main.controller.auth_controller import api as auth_ns

blueprint = Blueprint('api', __name__)
authorizations = {
  'api-key': {
    'type': 'apiKey',
    'in': 'header',
    'name': 'Authorization'
  }
}

api = Api(
  blueprint,
  title='MS-RBC',
  version='1.0',
  description='API access to an AI model for RBC detection',
  authorizations=authorizations,
  security='apikey'
)


# api.add_namespace(user_ns, path='/user')
# api.add_namespace(auth_ns)
api.add_namespace(status_ns, path='/status')
api.add_namespace(predict_ns, path='/predict')
api.add_namespace(auth_ns, path='/auth')
