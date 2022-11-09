from flask import Flask, render_template, redirect, request, Blueprint
import os
from models.models import models, db
from models.add_task import add_task

# Get base directory
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

# Set up db config to local path
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'test.db')

# Register db model blueprint
app.register_blueprint(models)

# Register add task blueprint
app.register_blueprint(add_task)

# Initialise db
db.init_app(app)
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
