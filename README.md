# flask_todo_app

# Basic Flask To Do App

### Using flask to create a basic CRUD functionality using blueprints to modularise the app. 

App layout is as follows:
app.py                       # Initial app file
requirements.txt
├── app                      # Folder containing all modularised app files
│   ├── forms
|   |   ├── forms.py         # File containing wtform classes
|   ├── models
|   |   ├── models.py        # File containing db model classes
|   ├── routes               # Folder containing each app URL route and its functionality
|   |   ├── add_task.py      
|   |   ├── delete_task.py
|   |   ├── update_task.py
|   ├── static
|   |   ├── css
|   |   |   ├── style.css    # File containing static css components
|   ├── templates            # Folder containing html templates
|   |   ├── add_task.html
|   |   ├── base.html
|   |   ├── home.html
|   |   ├── update_task.html

##### Worklow
There is a github workflow used on this repo to automatically style pull requests with pep8 styling convention. The workflow run fails if any changes are made and a new pull request is created containing the styling changes.
