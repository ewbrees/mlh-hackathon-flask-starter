from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

# I first made sure all the requirements were in agreeance with each other
# The removed all the contents of the app.py file and replaced with this simple hello world
# Ran these commands from a python terminal
# /home/codespace/.python/current/bin/python3 /workspaces/mlh-hackathon-flask-starter/app/app.py
# cd app
# export FLASK_SKIP_DOTENV=True
# export FLASK_APP=app.py
# flask run