from flask import Blueprint
from flask_sqlalchemy import SQLAlchemy

models = Blueprint('models', __name__)


db = SQLAlchemy()


# Set up db model
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(300), nullable=False)

    def __rep__(self):
        return '<Suggestion %r>' % self.id
