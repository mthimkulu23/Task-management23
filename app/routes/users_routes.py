from flask import Blueprint
from ..controllers import user_controllers

app = Blueprint('signup', __name__)


app.route('/signup', methods=['POST'])(user_controllers.signup)
app.route('/login', methods=['POST'])(user_controllers.login)
