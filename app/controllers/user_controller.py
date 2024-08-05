from flask import jsonify, request
import bcrypt
from ..models.users import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity, get_jwt


# The signup function handles the user registration process

def signup_user():
    
    username = request.json.get('username')
    contact = request.json.get('contact')
    email = request.json.get('email')
    password = request.json.get('password')

    if not username or not password:
        return jsonify({'message': 'Username and password are required'}), 400

 
    return jsonify({'message': 'User signed up successfully'}), 201


def login_user():
    username = request.json.get('username')
    password = request.json.get('password')

    if not username or not password:
        return jsonify({'message': 'Username and password are required'}), 400

    user = User.find_user_by_username(username=username).first()

    if not user or not User.check_password_hash(user.password, password):
        return jsonify({'message': 'Invalid username or password'}), 401

    access_token = create_access_token(identity=user.id)
    
    return jsonify({'message': 'Login successful', 'access_token': access_token}), 200

