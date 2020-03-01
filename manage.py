#flaskrを起動して実行するためのファイル
from __future__ import print_function
from flask_script import Manager
from flaskr import app, db

manager = Manager(app)

@manager.command
def init_db():
    db.create_all()

if __name__ == '__main__':
    manager.run()

# app.run(host='127.0.0.1', port=5000, debug=True)