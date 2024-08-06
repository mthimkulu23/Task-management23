from flask import Blueprint
from ..controllers import user_controllers

app = Blueprint('signup', __name__)


app.route('/signup', methods=['POST'])(user_controllers.signup_user)
# app.route('/login', methods=['POST'])(user_controller.login_user)
