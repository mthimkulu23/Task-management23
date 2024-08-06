from flask import jsonify
from .. import mongo



class users:

    def create_user(new_user):
        result = mongo.db.user.insert_one(new_user)
        return result
        
       