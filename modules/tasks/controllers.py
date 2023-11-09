from bson import ObjectId
from modules.common.functions import mongo_db

mongo = mongo_db()

class TasksController:

    def get_all(self):
        result = mongo.db.taskCollection.find()
        return result
    
    def get_one(self, task_id : str):
        result = mongo.db.taskCollection.find_one_or_404({'_id' : task_id})
        return result
    
    def create(self, task):
        insert = mongo.db.taskCollection.insert_one(task)
        return { 'object_id': insert.inserted_id }
    
    def update(self, task, task_id : str):
        mongo.db.taskCollection.update_one({'_id' : task_id}, {'$set' : task}, upsert=False)
        result = mongo.db.taskCollection.find_one_or_404({'_id' : task_id})
        return result
    
    def delete(self, task_id : str):
        mongo.db.taskCollection.delete_one({'_id' : task_id})
        return { 'message': 'Task eliminato' }
