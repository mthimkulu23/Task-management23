from bson.objectid import ObjectId
from .. import mongo  # Ensure mongo is properly imported



class UserAdmin:
    
    def find_user(query):
        return mongo.db.new_admin_user.find_one(query)
    
    def insert_user(cls, user_data):
        result = mongo.db.new_admin_user.insert_one(user_data)
        return result
    
    def create_user(cls, user_data):
        result = cls.insert_user(user_data)
        return result.inserted_id
    
    def get_user_by_email(cls, email):
        return cls.find_user({'email': email})
    
    def get_user_by_id(cls, user_id):
        if not ObjectId.is_valid(user_id):
            raise Exception('Invalid user ID')
        return cls.find_user({'_id': ObjectId(user_id)})
