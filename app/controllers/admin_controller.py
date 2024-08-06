from flask import jsonify,request
from werkzeug.security import generate_password_hash,check_password_hash
from ..models.admin import GetAdmin


def signup_admin():
    if request.method == 'POST':
        username = request.json.get('username')
        contact = request.json.get('contact')
        email = request.json.get('email')
        password = request.json.get('password')
        
        # if not username or not email or not password:
        #     return jsonify({'message': 'Username, email, and password are required'}), 400
        
        # Hash the password using Werkzeug's generate_password_hash()
        hashed_password = generate_password_hash(password)
        
        # Dictionary contain data 
        new_admin = {'username': username, 'contact': contact, 'email': email, 'password': hashed_password}
        
        GetAdmin.create_admin(new_admin)
        
        return jsonify({"message": "Successfully Signup as Admin"})
    

def login_admin():
    if request.method == 'POST':
        username = request.json.get('username')
        password = request.json.get('password')

        if not username or not password:
            return jsonify({'message': 'Username and password are required'}), 400

        admin = GetAdmin.get_admin_by_username(username)

        if not admin or not check_password_hash(admin['password'], password):
            return jsonify({'message': 'Invalid username or password'}), 401

        # Generate a JWT token or some other form of authentication token here

        return jsonify({'message': 'Login successful'})
    
    
    
    
    
 


