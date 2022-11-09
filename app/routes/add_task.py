from flask import Blueprint, request, redirect, render_template
from forms.forms import InputTodo, ToDoActions
from models.models import db, Todo
import requests

add_task = Blueprint('add_task', __name__)

# Create homepage


@add_task.route('/', methods=['POST', 'GET'])
def home():
    # Get forms
    form = InputTodo()
    actions = ToDoActions()
    if request.method == 'POST':
        if form.validate_on_submit:
            todo = Todo(content = form.content.data)
            try:
                db.session.add(todo)
                db.session.commit()
                return redirect('/')
            except BaseException:
                return 'There was an error while adding the task'
    else:
        # Show all tasks
        tasks = Todo.query.all()
        # Show homepage with all tasks
        return render_template("home.html", tasks=tasks, form = form, actions = actions)
