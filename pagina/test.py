from flask import Blueprint

bp = Blueprint('test',__name__)


@bp.route('/hola')
def index():
    return 'hola soy un blueprint'