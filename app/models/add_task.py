from flask import Blueprint, request, redirect, render_template
from models.models import db, Todo
import requests

add_task = Blueprint('add_task', __name__)

# Create homepage
@add_task.route('/', methods=['POST','GET'])
def home():
    # Add new task
    if request.method == 'POST':
        # Get content from form input
        task_content = request.form['content']
        new_task = Todo(content=task_content)

        try:
            # Add task to db
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an error while adding the task'

    else:
        # Show all tasks
        tasks = Todo.query.all()
        # Show homepage with all tasks
        return render_template("home.html", tasks=tasks)
