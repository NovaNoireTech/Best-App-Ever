from app import app

# from flask import Flask, request
# from uuid import uuid4

# app = Flask(__name__)

# users = {
#   '1': {
#     'username': 'kedwards',
#     'email' : 'kedwards@gmail.com'
#   },
#   '2' : {
#     'username': "kmassey",
#     'email': 'kmassey@gmail.com'
#   },
  
#   '3' : {
#     'username': "sglover",
#     'email': 'sglover@gmail.com'
#   }
# }

# customs = {
#   '1' : {
#     'text' : 'ALMOST THERE!!!',
#     'user_id': '1'
#   },
#   '2': {
#     'text': "WE GOT GRIT",
#     'user_id': '2'
#   },
#   '3':{
#     'text': 'WE DONT QUIT!!!!',
#     'user_id' : '1'
#   }
# }


# # user routes

# @app.get('/user')
# def user():
#   return { 'users': list(users.values()) }, 200

# @app.route('/user', methods=["CUSTOM"])
# def create_user():
#   json_body = request.get_json()
#   users[uuid4()] = json_body
#   return { 'message' : f'{json_body["username"]} created' }, 201

# # is this json_body change to text? assumning no but my post request on insomnia was not working

# @app.put('/user')
# def update_user():
#   return

# @app.delete('/user')
# def delete_user():
#   pass

# # customs routes

# @app.get('/custom')
# def get_customs():
#   return

# @app.post('/custom')
# def create_custom():
#   return

# @app.put('/custom')
# def update_custom():
#   return

# @app.delete('/custom')
# def delete_custom():
#   return