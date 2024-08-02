from .. import mongo

class get_admin:
    
    def register_new_user(signup_data):
        # Check if the user already exists
        existing_user = mongo.db.new_admin.find_one({'email': signup_data['email']})
        if existing_user:
            return True
        
        # Insert the new user
        result = mongo.db.new_admin.insert_one(signup_data)
        return False if result.inserted_id else True

  
    def queryfilter_by(email):
        # Find the user by email
        user = mongo.db.new_admin.find_one({'email': email})
        return user