from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .projects import Projects
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


def projects():
    # Instantiate the Projects class
    projects_instance = Projects()

    # Example: Get information for the "Sales Project"
    sales_project_data = projects_instance.get_project('sales_project')

    return render_template('projects.html', sales_project_data=sales_project_data)
