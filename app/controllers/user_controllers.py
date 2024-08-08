from flask import request, jsonify
from werkzeug.security import generate_password_hash,check_password_hash
from flask_jwt_extended import JWTManager, create_access_token
from ..models.users import User


def signup():
    if request.method == 'POST':
        username = request.json.get('username')
        email = request.json.get('email')
        password = request.json.get('password')
        role = request.json.get('role', 'user')  # Default to 'user' if no role is provided

        if User.find_by_email(email):
            return jsonify({"msg": "User already exists"}), 409

        hashed_password = generate_password_hash(password)

        # Create a new user object
        data = {"username": username,"email": email,"password": hashed_password,"role": role
        }

        user = User(**data)
        user.save()

        return jsonify({"message": "Successfully created Signup"}), 201


def login():
    if request.method == 'POST':
        email = request.json.get('email')
        password = request.json.get('password')

        user = User.find_by_email(email)
        print(f"User found: {user}")
        print(f"Hashed password: {user.password}")
        print(f"Provided password: {password}")

        if user and check_password_hash(user.password, password):
            access_token = create_access_token(identity={"email": user.email, "role": user.role})
            return jsonify({"access_token": access_token, "role": user.role ,"password":user.password}), 200
        else:
            return jsonify({"error": "Invalid email or password"}), 401

       

    
    

        
        

      


    
    
