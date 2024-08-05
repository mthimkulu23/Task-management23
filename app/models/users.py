from .. import mongo



class users:
    @staticmethod
    def find_user_by_username(username):
        # Implement your logic to find a user by username from the database
        existing_user = mongo.db.users.find_one({'username': username})
        return existing_user

    @staticmethod
    def create_user(username, email, password):
        existing_user = users.find_user_by_username(username)
        if existing_user:
            return None  # User already exists
        else:
            # Insert the new user into the database
             user_data = {'username': username, 'email': email, 'password': password}
             mongo.db.users.insert_one(user_data)
             return  user_data
        

