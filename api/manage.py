import os

import jwt
from app import blueprint
from app.main import create_app

app = create_app()
app.register_blueprint(blueprint)

app.app_context().push()
