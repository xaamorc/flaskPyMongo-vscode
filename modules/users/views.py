from http import HTTPStatus
from flask_smorest import Blueprint
from flask.views import MethodView
from modules.common.schemes import InsertedResponseSchema
from modules.users.controllers import UsersController

from modules.users.schemes import UsersSchema


users_blp = Blueprint(
    'users',
    'users_blp',
    url_prefix='/users',
    description = "Users REST blueprint"
)

@users_blp.route('')
class UsersApi(MethodView):
    
        @users_blp.response(HTTPStatus.OK, UsersSchema(many=True))
        def get(self):
            """Get users"""
            controller = UsersController()
            return controller.get_all()
        
        @users_blp.arguments(UsersSchema)
        @users_blp.response(HTTPStatus.CREATED, InsertedResponseSchema)
        def post(self, user):
            """Create a new user"""
            controller = UsersController()
            return controller.create(user)
        
@users_blp.route('/<string:user_id>')
class UserApi(MethodView):
        
        @users_blp.response(HTTPStatus.OK, UsersSchema)
        def get(self, user_id):
            """Get a user"""
            controller = UsersController()
            return controller.get(user_id)
            
        @users_blp.arguments(UsersSchema)
        @users_blp.response(HTTPStatus.OK, UsersSchema)
        def put(self, user, user_id):
            """Update a user"""
            controller = UsersController()
            return controller.update(user_id, user)
            
        @users_blp.response(HTTPStatus.NO_CONTENT)
        def delete(self, user_id):
            """Delete a user"""
            controller = UsersController()
            return controller.delete(user_id)