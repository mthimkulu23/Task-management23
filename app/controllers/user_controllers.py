from flask import request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta
from ..models.users import User_admin
import jwt
import os


# def register_admin(username, password, email):
#     user_data = {
#         'username': username,
#         'email': email,
#         'password': password,
#         'role': 'admin'
#     }
#     result = User_admin.create_user(user_data)
#     return result

# def register_user(username, password, email):
#     user_data = {
#         'username': username,
#         'email': email,
#         'password': password,
#         'role': 'user'
#     }
#     result = User_admin.create_user(user_data)
#     return result

def signup():
    if request.method == 'POST':
        username = request.json.get('username')
        email = request.json.get('email')
        password = request.json.get('password')
        role = request.json.get('role')

       
        hashed_password = generate_password_hash(password)

        # if role == 'admin':
        #     user_id = register_admin(username, hashed_password, email)
        # else:
        #     user_id = register_user(username, hashed_password, email)

        payload = {
            'user_id': user_id,
            'role': role,
            'exp': datetime.utcnow() + timedelta(hours=1)
        }
        token = jwt.encode(payload, os.environ.get('SECRET_KEY'), algorithm='HS256')

        return jsonify({'token': token.decode('utf-8')}), 201
    else:
        return jsonify({"message":"Successfully Signup"})

def login_user():
    email = request.json.get('email')
    password = request.json.get('password')

    user = User_admin.get_user_by_email(email)

    if user and check_password_hash(user['password'], password):
        payload = {
            'user_id': str(user['_id']),
            'role': user['role'],
            'exp': datetime.utcnow() + timedelta(hours=1)
        }
        token = jwt.encode(payload, os.environ.get('SECRET_KEY'), algorithm='HS256')

        return jsonify({'token': token.decode('utf-8')}), 200
    else:
        return jsonify({'error': 'Invalid username or password'}), 401
    
    
