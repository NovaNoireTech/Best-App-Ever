# from datetime import datetime, timezone

# from app import db
# from models.user_model import UserModel

# class CustomModel(db.Model):

#   __tablename__ = 'customs'

#   id = db.Column(db.Integer, primary_key = True)
#   text = db.Column(db.String, nullable = False)
#   timestamp = db.Column(db.String)
#   user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)

#   def __repr__(self):
#     return f'<Custom: {self.text}>'
  
#   def commit(self):
#     db.session.add(self)
#     db.session.commit()

#   def delete(self):
#     db.session.delete(self)
#     db.session.commit()