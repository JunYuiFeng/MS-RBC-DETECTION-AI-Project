import sqlite3
from flask import g, current_app

DB = 'database.db'

def get_db():
  db = getattr(g, '_database', None)
  if db is None:
    db = g._database = sqlite3.connect(DB)
  return db
     
def init_db():
  with current_app.app_context():
    db = get_db()
    with current_app.open_resource('../../schema.sql', mode='r') as f:
      db.cursor().executescript(f.read())
    db.commit()

    
def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv   