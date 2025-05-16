# Task Management - User Authentication Module

This module provides user signup and login functionality for the Task Management system using MongoDB and JWT-based authentication.

# 📌 Features

User registration (signup)

Secure password hashing using Werkzeug

JWT-based login and access control

User role management (e.g., admin, user)

# 🧱 Tech Stack

Python + Flask

MongoDB

Flask-JWT-Extended

Werkzeug security utilities

Flask-PyMongo


# 🚀 API Endpoints

🔐 Signup – POST /signup
Registers a new user.

Request:

json

Copy

Edit
{
  "username": "johndoe",
  "email": "johndoe@example.com",
  "password": "yourPassword",
  "role": "user"
}

# 🧠 User Class Reference

__init__(self, email, username, password, role)

Initializes a User object.

save(self)

Saves the user data to MongoDB.

find_by_email(email)

Retrieves a user document by email and returns a User object if found.
