from flask import request, jsonify
from werkzeug.security import generate_password_hash
from flask_jwt_extended import JWTManager, create_access_token
from ..models.users import User_admin





def signup():
    if request.method == 'POST':
        username = request.json.get('username')
        email = request.json.get('email')
        password = request.json.get('password')
        role = request.json.get('role')
        
        hashed_password = generate_password_hash(password)
        
        data = {"username": username, "email": email, "password": hashed_password, "role": role}
        User_admin.create_user(data)
        
        access_token = create_access_token(identity={"email": email, "role": role})
        return jsonify({"message": "Successfully created Signup", "access_token": access_token})
    
    

        
        

      


    
    
