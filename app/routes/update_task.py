from flask import Blueprint, request, redirect, render_template
from forms.forms import InputTodo, ToDoActions
from models.models import db, Todo
import requests

update_task = Blueprint('update_task', __name__)

# Create URL for updating task


@update_task.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    task = Todo.query.get_or_404(id)

    form = InputTodo()
    actions = ToDoActions()
    tasks = Todo.query.all()

    if request.method == 'POST':
        task.content = request.form['content']

        try:
            db.session.commit()
            # Return to homepage
            return redirect('/')
        except BaseException:
            return 'There was an issue while updating that task'

    else:
        # Show update task page
        return render_template('update_task.html', tasks=tasks, task=task, form = form, actions = actions)
