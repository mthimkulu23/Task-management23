from flask import Flask
from flask_pymongo import PyMongo
from flask_jwt_extended import JWTManager
from .config import Config

mongo = PyMongo()

def building_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # initializes the PyMongo instance with the Flask application, allowing the application to use the MongoDB database.
    mongo.init_app(app)
    
    
    
# JWT Initialization
    jwt = JWTManager(app)
   
    with app.app_context():
        # this block used to ensure that the application context is available when registering the application blueprints
        from .routes import users_routes
     
         
    # register blueprint for signup
        app.register_blueprint(users_routes.app)
       
       
      
    
    return app

