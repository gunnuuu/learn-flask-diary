from flask import Blueprint

# Create Blueprint
auth = Blueprint('auth', __name__)

# route
@auth.route('/')
def home():
    return '<h1>home</h1>'