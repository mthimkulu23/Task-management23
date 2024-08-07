from bson.objectid import ObjectId
from .. import mongo  # Ensure mongo is properly imported



class User_admin:
    
 
    def find_user(query):
        return mongo.db.new_admin_user.find_one(query)
    
   
    def insert_user(user_data):
        result = mongo.db.new_admin_user.insert_one(user_data)
        return result
    

    def create_user(user_data):
        return mongo.db.new_admin_user.insert_one(user_data)
    

    def get_user_by_email(email):
        return User_admin.find_user({'email': email})
    

    def get_user_by_id(user_id):
        if not ObjectId.is_valid(user_id):
            raise Exception('Invalid user ID')
        return User_admin.find_user({'_id': ObjectId(user_id)})
