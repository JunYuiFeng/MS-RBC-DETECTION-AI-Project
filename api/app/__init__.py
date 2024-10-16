from flask import Blueprint
from flask_restx import Api

from .main.controller.predict_controller import api as predict_ns
from .main.controller.compare_controller import compare_api as compare_ns
from .main.controller.auth_controller import api as auth_ns
from .main.controller.users_controller import api as users_ns
from .main.controller.user_controller import api as user_ns


# create API bluepring
blueprint = Blueprint('api', __name__)
authorizations = {
  'jsonWebToken': {
    'type': 'apiKey',
    'in': 'header',
    'name': 'Authorization'
},
}

api = Api(
  blueprint,
  title='MS-RBC',
  version='1.0',
  description='API access to an AI model for RBC detection',
  authorizations=authorizations,
  security='apikey'
)


#namespaces for different controllers
api.add_namespace(predict_ns, path='/predict')
api.add_namespace(compare_ns, path='/compare')
api.add_namespace(auth_ns, path='/auth')
api.add_namespace(users_ns, path='/users')
api.add_namespace(user_ns, path='/user')
