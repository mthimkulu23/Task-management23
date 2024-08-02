from flask import jsonify, request,json
from ..models.admin import get_admin
import bcrypt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity, get_jwt


# The signup function handles the user registration process

def admin_signup():
    user_admin ={
    'username':request.json.get('username'),
     'contact':request.json.get('contact'),
      'email':request.json.get('email'),
       'password':request.json.get('password')
       
}
    

    # Check if the admin is signing up for the first time
    current_user_id = get_jwt_identity()
    if current_user_id is None:
        # register_new_admin method from the Admin model
        if not get_admin.register_new_user(user_admin):
            return jsonify({'message': 'Signup Success'})
        else:
            return jsonify({'message': 'Signup Failed'}), 400
    else:
        return jsonify({'message': 'You are already signed up'}), 400
    
    


# The login function handles the login_admin process
def admin_login():
    data = request.get_json()
    email = data['email']
    password = data['password']
    print('Received data:', email, password)

    user = get_admin.queryfilter_by(email=email).first()

    if user and bcrypt.check_password_hash(user.password, password):
        # Check if the user exists and the password is correct
        access_token = create_access_token(identity=user.id)
        # Create an access token using the user's ID
        return jsonify({'message': 'Login Success', 'access_token': access_token})
    else:
        return jsonify({'message': 'Login Failed'}), 401