from flask_wtf import FlaskForm 
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired

class InputTodo(FlaskForm):
    """Todo Input form."""
    content = StringField(
        'Task',
        validators=[InputRequired()]
    )
    submit = SubmitField('Add task')

class ToDoActions(FlaskForm):
    """Todo Actions form."""
    update = SubmitField('Update')
    delete = SubmitField('Delete')
