from flask import jsonify,request
from ..models.users import users


def signup_user():
   if request.method == 'POST':
    username = request.json.get('username')
    contact = request.json.get('contact')
    email = request.json.get('email')
    password = request.json.get('password')
    
    if not contact or not username or not email or not password :
        return jsonify({'message': 'Username, email, and password are required'}), 400
    
    
    new_user = {
        'username': username,'email': email,'password': password,
    }
    
    users.create_user(new_user)
       
    return jsonify({"success": True})