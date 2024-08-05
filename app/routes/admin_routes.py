from flask import Blueprint
from ..controllers import admin_controller

app = Blueprint('admin_signup', __name__)



app.route('/admin_get_signup', methods=['POST'])(admin_controller.admin_signup)
app.route('/admin_get_login', methods=['POST'])(admin_controller.admin_login)