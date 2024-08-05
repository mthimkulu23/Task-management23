from flask import jsonify,request
from flask_jwt_extended import get_jwt_identity, create_access_token
import bcrypt
from ..models.admin import get_admin

def admin_signup():
    # Get the JSON data from the request
    admin_data = {
        'username': request.json.get('username'),
        'contact': request.json.get('contact'),
        'email': request.json.get('email'),
        'password': request.json.get('password')
    }

    try:
        # Check if the admin already exists
        if get_admin.register_new_user(admin_data):
            return jsonify({'message': 'Admin already exists'}), 409

        # Hash the password
        admin_data['password'] = bcrypt.generate_password_hash(admin_data['password']).decode('utf-8')

        # Insert the new admin
        get_admin.register_new_user(admin_data)

        return jsonify({'message': 'Admin created successfully'}), 201
    except Exception as e:
        return jsonify({'message': 'Signup Failed', 'error': str(e)}), 400
    
    
def admin_login():
    # Get the JSON data from the request
    admin_login = {
        'email': request.json.get('email'),
        'password': request.json.get('password')
    }

    try:
        # Check if the user exists and the password is correct
        user = get_admin.queryfilter_by(email=admin_login['email']).first()
        if user and bcrypt.check_password_hash(user.password, admin_login['password']):
            # Create an access token using the user's ID
            access_token = create_access_token(identity=user.id)
            return jsonify({'message': 'Login Successful', 'access_token': access_token})
        else:
            return jsonify({'message': 'Login Failed'}), 401
    except Exception as e:
        return jsonify({'message': 'Login Failed', 'error': str(e)}), 401


