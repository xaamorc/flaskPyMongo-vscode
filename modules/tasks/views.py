from http import HTTPStatus
from flask import Blueprint
from flask.views import MethodView
from modules.tasks.controllers import TasksController
from modules.tasks.schemes import TaskSchema


tasks_blp = Blueprint(
    'tasks',
    'tasks_blp',
    url_prefix='/tasks',
    description= 'Tasks REST blueprint'
)

@tasks_blp.route('')
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
    
@tasks_blp.route('/<string:task_id>')
class TaskApi(MethodView):

    @tasks_blp.response(HTTPStatus.OK, TaskSchema)
    def get(self, task_id):
        """Get a task"""
        controller = TasksController()
        return controller.get(task_id)
    
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
    

