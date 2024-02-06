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

@views.route('/coming_soon/<tag>')
def coming_soon(tag):
    return render_template('coming_soon.html', tag=tag)


@views.route('/')
def home():
    return render_template('home.html')

@views.route('/about/')
def about():
    return render_template('about.html')

@views.route('/projects/<project_name>')
def projects(project_name):
    # Specify the path to your project data file
    project_data_file = 'website/projects.json'
    
    # Create an instance of the Projects class
    projects_instance = Projects(project_data_file)
    
    # Retrieve project information based on the dynamic project name
    project_info = projects_instance.get_project(project_name)
    
    # Check if the project exists
    if project_info:
        return render_template('projects.html', projects_data=project_info)
    else:
        flash(f'Project "{project_name}" not found', 'error')
        return render_template('home.html')
