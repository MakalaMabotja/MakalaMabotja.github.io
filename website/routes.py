from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
# from .models import Note
# from . import db
import json

routes = Blueprint('routes', __name__)