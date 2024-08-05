from .. import mongo

class GetAdmin:
    @staticmethod
    def check_if_admin_exists(username):
        # Check if the admin already exists
        existing_admin = mongo.db.new_admin.find_one({'username': username})
        return existing_admin is not None

    @staticmethod
    def register_new_user(user_admin):
        # Insert the new user
        result = mongo.db.new_admin.insert_one(user_admin)
        return result.inserted_id is not None

    @staticmethod
    def query_by_email(email):
        # Find the user by email
        user = mongo.db.new_admin.find_one({'email': email})
        return user
