from .. import mongo

class GetAdmin:
    def create_admin(new_admin):
        return mongo.db.admin_collection.insert_one(new_admin)
    
    def get_admin_by_username(username):
        admin = mongo.db.admin_collection.find_one({'username': username})
        return admin
