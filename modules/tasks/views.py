from http import HTTPStatus
from flask import render_template
# from modules.common.functions import mongo_db
from flask_smorest import Blueprint
from flask.views import MethodView
from modules.tasks.controllers import TasksController
from modules.tasks.schemes import TaskSchema

# mongo = mongo_db()

tasks_blp = Blueprint(
    'tasks',
    'tasks_blp',
    description= 'Tasks REST blueprint',
    template_folder='views',
)

@tasks_blp.route('/tasks')
class TasksApi(MethodView):

    @tasks_blp.response(HTTPStatus.OK, TaskSchema(many=True))
    def get(self):
        """Get tasks"""
        controller = TasksController()
        return controller.get_all()
    
    @tasks_blp.arguments(TaskSchema)
    @tasks_blp.response(HTTPStatus.CREATED, TaskSchema)
    def post(self, task):
        """Create a new task"""
        controller = TasksController()
        return controller.create(task)
    
@tasks_blp.route('/task/<string:task_id>')
class TaskApi(MethodView):

    @tasks_blp.response(HTTPStatus.OK, TaskSchema)
    def get(self, task_id):
        """Get a task"""
        controller = TasksController()
        return controller.get_one(task_id)
    
    @tasks_blp.arguments(TaskSchema)
    @tasks_blp.response(HTTPStatus.OK, TaskSchema)
    def put(self, task, task_id):
        """Update a task"""
        controller = TasksController()
        return controller.update(task_id, task)
    
    @tasks_blp.response(HTTPStatus.NO_CONTENT)
    def delete(self, task_id):
        """Delete a task"""
        controller = TasksController()
        return controller.delete(task_id)
    
@tasks_blp.route('/tasksUi')
@tasks_blp.response(HTTPStatus.OK, TaskSchema)
def get():
    """Get tasks UI"""
    controller = TasksController()
    tasks = controller.get_all()
    return render_template('tasks.html', tasks=tasks) 

   

@tasks_blp.route('/tasksUi/<string:task_id>')
@tasks_blp.response(HTTPStatus.OK, TaskSchema)
def get(task_id):
    """Get task UI"""
    controller = TasksController()
    task = controller.get_one(task_id)
    return render_template('task.html', task=task)