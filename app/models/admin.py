from .. import mongo

class get_admin:
    def register_new_user( user_admin):
        # Check if the user already exists
        existing_user = mongo.db.new_admin.find_one({'email':  user_admin['email']})
        if existing_user:
            return True
        
        # Insert the new user
        result = mongo.db.new_admin.insert_one(user_admin)
        return False if result.inserted_id else True

    def queryfilter_by(email):
        # Find the user by email
        user = mongo.db.new_admin.find_one({'email': email})
        return user