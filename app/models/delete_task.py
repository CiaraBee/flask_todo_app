from flask import Blueprint, request, redirect, render_template
from models.models import db, Todo
import requests

delete_task = Blueprint('delete_task', __name__)


@delete_task.route('/delete/<int:id>')
def delete(id):
    # Get ID of item to delete
    task_to_delete = Todo.query.get_or_404(id)
    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except BaseException:
        return 'There was an error while deleting that task'
