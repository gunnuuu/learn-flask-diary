from flask import Flask

# Create App
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'smicircle_secret_key'

    return app