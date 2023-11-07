from bson import ObjectId
from modules.common.functions import mongo_db

mongo = mongo_db()

class UsersController:
    def get_all(self):
        result = mongo.db.usersCollection.find()
        return result
    
    def get_one(self, user_id : str):
        result = mongo.db.usersCollection.find_one_or_404({'_id' : ObjectId(user_id)})
        return result
    
    def create(self, user):
        insert = mongo.db.usersCollection.insert_one(user)
        return { 'object_id': insert.inserted_id }
    
    def update(self, user, user_id : str):
        mongo.db.usersCollection.update_one({'_id' : ObjectId(user_id)}, {'$set' : user}, upsert=False)
        result = mongo.db.usersCollection.find_one_or_404({'_id' : ObjectId(user_id)})
        return result
    
    def delete(self, user_id : str):
        mongo.db.usersCollection.delete_one({'_id' : ObjectId(user_id)})
        return { 'message': 'Utente eliminato' }