from flask import Blueprint

service = Blueprint('credit', __name__)
from .views import *