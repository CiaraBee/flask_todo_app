from flask import Flask, render_template, redirect, request, Blueprint
import os
from models.models import models, db
from routes.add_task import add_task
from routes.update_task import update_task
from routes.delete_task import delete_task
from forms.forms import InputTodo

# Get base directory
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

# Set up db config to local path
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'test.db')

app.config['SECRET_KEY'] = 'secret'

# Register db model blueprint
app.register_blueprint(models)

# Register add task blueprint
app.register_blueprint(add_task)

# Register update task blueprint
app.register_blueprint(update_task)

# Register update task blueprint
app.register_blueprint(delete_task)

# Initialise db
db.init_app(app)
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
