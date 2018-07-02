from flask import Flask

# Initialize the app
app = Flask(__name__, instance_relative_config=True)

# Load the views
from app import views

# load the outh modeul
from app import oauth

# Load the config file
app.config.from_object('config')

