from flask import g
from app import blueprint
from app.main import create_app

DB = 'database.db'

app = create_app()
app.register_blueprint(blueprint)
app.app_context().push()


# close db connection
@app.teardown_appcontext
def close_connection(exception):
  db = getattr(g, '_database', None)
  if db is not None:
    db.close()   
    
