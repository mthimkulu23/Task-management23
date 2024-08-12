from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash
from .. import mongo  

class User:
    def __init__(self, email, username, password, role):
        # The __init__ method initializes a new User object with the provided email, username, password, and role.
        self.email = email
        self.username = username
        self.password = password
        self.role = role

    def save(self):
        # The save method is responsible for saving the user data to the database.
        mongo.db.new_admin_user.insert_one({
            "email": self.email,
            "username": self.username,
            "password": self.password,
            "role": self.role
            # The role attribute stores the user's role, which can be 'user' or another custom role.
        })

  
    def find_by_email(email):
        # The find_by_email method is a static method that retrieves a user by their email address.
        user_data = mongo.db.new_admin_user.find_one({"email": email})
        if user_data:
            # If a user is found, it creates a new User object with the retrieved data and returns it.
            return User(
                email=user_data['email'],
                username=user_data['username'],
                password=user_data['password'],
                role=user_data['role']
            )
        return None
   