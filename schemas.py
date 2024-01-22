from marshmallow import Schema, fields

class UserSchema(Schema):
  id = fields.Str(dump_only = True)
  email = fields.Str(required = True)
  username = fields.Str(required = True)
  password = fields.Str(required = True, load_only = True )
  first_name = fields.Str()
  last_name = fields.Str()

class UserLogin(Schema):
  username = fields.Str(required = True)
  password = fields.Str(required = True, load_only = True )

class CustomSchema(Schema):
  id = fields.Str(dump_only = True)
  text = fields.Str(required = True)
  timestamp = fields.DateTime(dump_only = True)

class CustomSchemaNested(CustomSchema):
  user = fields.Nested(UserSchema, dump_only = True)

class UserSchemaNested(UserSchema):
  customs = fields.List(fields.Nested(CustomSchema), dump_only=True)

  # pick up on day 6