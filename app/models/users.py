
from .. import mongo



class users:
    
      
    def create_user(new_user):
        try:
            # Insert the new user document into the 'users' collection
            result = mongo.db.user.insert_one(new_user)
            return result.inserted_id
        except Exception as e:
            # Handle any errors that occur during the insert operation
            print(f"Error creating user: {e}")
            return None