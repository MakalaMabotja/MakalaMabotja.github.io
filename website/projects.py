import json

class Projects:
    def __init__(self, project_file_path):
        # Load project data from the specified JSON file
        with open(project_file_path, 'r') as file:
            self.projects_data = json.load(file)

    def get_project(self, project_name):
        # Retrieve information for a specific project
        return self.projects_data.get(project_name, None)
