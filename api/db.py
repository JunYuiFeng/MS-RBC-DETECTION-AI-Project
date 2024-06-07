import sqlite3
import os.path
from flask import g, current_app
import json
import logging
logging.basicConfig(level=logging.DEBUG)


DB = './database.db'

def get_db():
  db = getattr(g, '_database', None)
  if db is None:
    db = g._database = sqlite3.connect(DB)
    db.row_factory = sqlite3.Row
  return db
     
def init_db():
  if os.path.isfile(DB):
    return None

  with current_app.app_context():
    db = get_db()
    with current_app.open_resource('../../schema.sql', mode='r') as f:
      db.cursor().executescript(f.read())
    db.commit()

    
def query_db(query, args=(), bool=False, mod=False):
    db = get_db()
    try:
        cur = db.execute(query, args)
        if mod:
            cur.close()
            db.commit()
            return None
        # handle SELECT exists statements
        if bool:
            bool_res = cur.fetchall()
            db.commit()
            return bool_res
        # Fetch column descriptions and rows
        cols = [description[0] for description in cur.description]
        rv = cur.fetchall()  
        if not cols:
            return []
        result = [dict(zip(cols, row)) for row in rv]
        return result
    except sqlite3.Error as e:
        logging.error(f"SQLite error: {e}")
        return []
    finally:
        cur.close()
  
  
def to_json(response, cursor):
  cols = [description[0] for description in cursor.description]
  result = [dict(zip(cols, row)) for row in response]
  
  return json.dumps(result, indent=4)