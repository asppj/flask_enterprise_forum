from flask import Blueprint

nav_blueprint = Blueprint('home', __name__)
from . import view
