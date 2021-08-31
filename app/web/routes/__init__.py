from flask import Blueprint
routes = Blueprint('routes', __name__)

from web.routes.ride_api import *