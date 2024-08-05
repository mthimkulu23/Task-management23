from .. import mongo

# The Users model
class users:
    
   
    def register_new_user(signup_data):
        # Check if the user already exists
        existing_user = mongo.db.new_user.find_one({'email': signup_data['email']})
        if existing_user:
            return True
        
        # Insert the new user
        result = mongo.db.new_user.insert_one(signup_data)
        return False if result.inserted_id else True

  
    def queryfilter_by(email):
        # Find the user by email
        user = mongo.db.new_user.find_one({'email': email})
        return user
        

