from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash


from .. import mongo  

class User:
    def __init__(self, email, username, password, role):
        self.email = email
        self.username = username
        self.password = password
        self.role = role

    def save(self):
        mongo.db.new_admin_user.insert_one({
            "email": self.email,
            "username": self.username,
            "password": self.password,
            "role": self.role
        })

  
    def find_by_email(email):
        user_data = mongo.db.new_admin_user.find_one({"email": email})
        if user_data:
            return User(
                email=user_data['email'],
                username=user_data['username'],
                password=user_data['password'],
                role=user_data['role']
            )
        return None
   