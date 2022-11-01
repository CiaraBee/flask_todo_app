from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
import os
import requests

#Get base directory
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

#Set up db config to local path
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'test.db')
db = SQLAlchemy(app)

#Set up db model
class lunchPicker(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(300), nullable=False)

    def __rep__(self):
        return '<Suggestion %r>' % self.id

# Create db
from app import db
with app.app_context():
    db.create_all()

# Create homepage
@app.route('/', methods=['POST','GET'])
def home():
    if request.method == 'POST':
        task_content = request.form['content']
        new_task = lunchPicker(content=task_content)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an error while adding the task'

    else:
        tasks = lunchPicker.query.all()
        return render_template("home.html", tasks=tasks)

if __name__ == "__main__":
    app.run(debug=True)