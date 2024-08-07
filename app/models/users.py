from bson.objectid import ObjectId
from .. import mongo  # Ensure mongo is properly imported


class User_admin(mongo.Document):
    username = mongo.StringField(required=True, unique=True)
    email = mongo.EmailField(required=True, unique=True)
    password = mongo.StringField(required=True)
    role = mongo.StringField(required=True, default='admin')

    def __init__(self, username, email, password, role):
        self.username = username
        self.email = email
        self.password = password
        self.role = role

    def __repr__(self):
        return f'<User_admin {self.username}>'

    def to_dict(self):
        mongo.db.new_admin_user.insert_one({
     
            "username": self.username,
            "email": self.email,
            "password": self.password,
            "role": self.role
        })
        
