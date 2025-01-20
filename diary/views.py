from flask import Blueprint

# Create Blueprint
views = Blueprint('views', __name__)

# route
@views.route('/sign-up')
def sign_up():
    return '<h1>sign-up</h1>'

@views.route('/logout')
def logout():
    return '<h1>logout</h1>'

@views.route('/sign-in')
def sign_in():
    return '<h1>sign-in</h1>'