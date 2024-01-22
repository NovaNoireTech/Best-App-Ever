from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity
from uuid import uuid4
from flask.views import MethodView
from flask_smorest import abort

from models import CustomModel
from schemas import CustomSchema, CustomSchemaNested

from . import bp
# custom routes

@bp.route('/<custom_id>')
class Custom(MethodView):

  @bp.response(200, CustomSchemaNested)
  def get(self, custom_id):
    custom = CustomModel.query.get(custom_id)
    if custom:
      # print(custom.author)
      return custom
    abort(400, message='Invalid Custom')

  @jwt_required
  @bp.arguments(CustomSchema)
  def put(self, custom_data, custom_id):
    custom = CustomModel.query.get(custom_id)
    if custom and custom.user_id == get_jwt_identity():
      custom.body = custom_data['text']
      custom.commit()
    return {'message': "Invalid Custom Id"}, 400

  @jwt_required()
  def delete(self, custom_id):
    custom = CustomModel.query.get(custom_id)
    if custom and custom.user_id == get_jwt_identity():
      custom.delete()
      return {"message": "Custom Deleted"}, 202
    return {'message':"Invalid Custom or User"}, 400

@bp.route('/')
class CustomList(MethodView):

  @bp.response(200, CustomSchema(many = True))
  def get(self):
    return CustomModel.query.all()
  
  @jwt_required()
  @bp.arguments(CustomSchema)
  def custom(self, custom_data):
    try:
      custom = CustomModel()
      custom.user_id = get_jwt_identity()
      custom.body = custom_data['text']
      custom.commit()
      return { 'message': "Custom Created" }, 201
    except:
      return { 'message': "Invalid User"}, 401