from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
# from .models import Note
# from . import db
import json

views = Blueprint('views', __name__)

@views.route('/design')
def design():
    return render_template('elements.html')

@views.route('/')
def home():
    return render_template('home.html')

@views.route('/about/')
def about():
    return render_template('about.html')


@views.route('/projects/')
def projects():

    return render_template('projects.html')
