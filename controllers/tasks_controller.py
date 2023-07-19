from flask import render_template, Blueprint, request
from models.task_list import tasks, add_new_task
from models.task import Task

tasks_blueprint = Blueprint("tasks", __name__)

@tasks_blueprint.route('/tasks')
def index():
    return render_template('index.jinja', title='My Task List', tasks=tasks)

@tasks_blueprint.route('/tasks', methods=['POST'])
def add_task():
    task_title = request.form['title']
    task_description = request.form['description']
    new_task = Task(task_title, task_description, False)
    add_new_task(new_task)
    return render_template('index.jinja', title="My Task List", tasks=tasks)