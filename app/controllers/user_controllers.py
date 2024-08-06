from flask import jsonify,request
from werkzeug.security import generate_password_hash
from ..models.users import users


def signup_user():
    if request.method == 'POST':
        username = request.json.get('username')
        contact = request.json.get('contact')
        email = request.json.get('email')
        password = request.json.get('password')
        
        if not username or not email or not password:
            return jsonify({'message': 'Username, email, and password are required'}), 400
        
        # Hash the password using Werkzeug's generate_password_hash()
        hashed_password = generate_password_hash(password)
        
        # Added the 'contact' field
        new_user = {'username': username, 'contact': contact, 'email': email, 'password': hashed_password}
        
        users.create_user(new_user)
        
        return jsonify(new_user)