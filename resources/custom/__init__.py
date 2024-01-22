from flask_smorest import Blueprint

bp = Blueprint('customs', __name__, description='Ops on Customs', url_prefix='/custom')

from . import routes