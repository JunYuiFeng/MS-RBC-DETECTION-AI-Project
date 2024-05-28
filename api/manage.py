import os

from app import blueprint
from app.main import create_app

app = create_app()
app.register_blueprint(blueprint)

app.app_context().push()

# if __name__ == '__main__':
#     app.run(debug=True)
