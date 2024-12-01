from utils.response import json
from flask import Blueprint, redirect # type: ignore

main_bp = Blueprint('main', __name__)

default_route = '/api/v1/'

@main_bp.route("/")
def checker():
    return redirect(default_route)

@main_bp.route(default_route)
def index():
    return json(True, 'Welcome to the API', 200)
