from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash

from .. import mongo  


class User_admin():
    def __init__(self, username, email, password, role='user'):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)
        self.role = role
        
    def save(self):
        # Insert the user document into the 'new_admin_user' collection
        mongo.db.new_admin_user.insert_one({
            "username": self.username,
            "email": self.email,
            "password": self.password,
            "role": self.role
        })

   
    def find_by_email(cls, email):
        user = mongo.db.new_admin_user.find_one({"email": email})
        return user

    @staticmethod
    def create_user(data):
        user = User_admin(
            username=data.get('username'),
            email=data.get('email'),
            password=data.get('password'),
            role=data.get('role', 'user')
        )
        user.save()
    
    
    



