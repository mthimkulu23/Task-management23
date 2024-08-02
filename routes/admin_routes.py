from flask import Blueprint
from ..controllers import admin_controller

app = Blueprint('signup', __name__)



app.route('/admin_signup', methods=['POST'])(admin_controller.admin_signup)
app.route('/admin_login', methods=['POST'])(admin_controller.admin_login)