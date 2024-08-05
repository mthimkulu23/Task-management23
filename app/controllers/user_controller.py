from flask import jsonify, request
from ..models.users import users
import bcrypt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity, get_jwt


# The signup function handles the user registration process

def signup_user():
    # Get the JSON data from the request
    username = request.json.get('username')
    contact = request.json.get('contact')
    email = request.json.get('email')
    password = request.json.get('password')

    # Check if the user is signing up for the first time
    current_user = users.queryfilter_by(email)
    if current_user is None:
        # Call the register_new_user method from the Users model
        if users.register_new_user(username, contact, email, password):
            return jsonify({'message': 'Signup Success'}), 201
        else:
            return jsonify({'message': 'Signup Failed'}), 400
    else:
        return jsonify({'message': 'You are already signed up'}), 400