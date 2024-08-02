from flask import Flask
from flask_pymongo import PyMongo
from .config import Config


mongo = PyMongo()

def building_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    

    mongo.init_app(app)
    
    with app.app_context():
        from .routes import users_routes
        from .routes import admin_routes
        
        app.register_blueprint(users_routes.app)
        app.register_blueprint(admin_routes.app)
        
        return app

