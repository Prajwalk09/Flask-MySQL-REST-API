from app import app
from Model.user_model import user_model
from flask import request

obj = user_model()
@app.route('/users/getall')
def user_getall_controller():
    return obj.user_getall_model()

@app.route('/users/addone', methods = ["POST"])
def user_addone_controller():
    return obj.user_addone_model(request.form)

@app.route('/users/update', methods = ['PUT'])
def user_update_controller():
    return obj.user_updateone_model(request.form)

@app.route('/users/delete/<id>', methods = ['DELETE'])
def user_delete_controller(id):
    return obj.user_delete_model(id)

@app.route('/users/patch/<id>', methods = ['PATCH'])
def user_patch_controller(id):
    return obj.user_patch_model(request.form, id)

@app.route('/users/getall/limit/<limit>/page/<page>', methods = ['GET'])
def user_pagination_controller(limit, page):
    return obj.user_pagination_model(limit, page)