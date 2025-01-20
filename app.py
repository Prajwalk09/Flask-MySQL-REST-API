from flask import Flask

app = Flask(__name__)

@app.route('/')
def welcome():
    return "Hello World! This is a page!!"

@app.route('/products')
def products():
    return "Products Page!"

# import Controller.user_controller
# import Controller.prdocut_controller

# from Controller import user_controller, prdocut_controller

from Controller import *

