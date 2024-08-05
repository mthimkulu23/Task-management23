from flask import Blueprint
from ..controllers import user_controller

app = Blueprint('signup', __name__)


app.route('/signup', methods=['GET','POST'])(user_controller.signup)
app.route('/login', methods=['GET','POST'])(user_controller.login)
