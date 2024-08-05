from flask import Blueprint
from ..controllers import user_controller

app = Blueprint('signup', __name__)


app.route('/signup', methods=['POST'])(user_controller.signup_user)
# app.route('/login', methods=['POST'])(user_controller.login_user)
