import os
import sys


def create_project_structure(project_name, *args):
    # Get the current script directory
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Define the parent directory where the new project should be created
    parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))

    # Define the base folder names
    base_folders = ["MATLAB", "LTSpice", "KiCAD", "EasyEDA", "Python", "Arduino"]

    # Create the main project directory outside the current folder
    project_path = os.path.join(parent_dir, project_name)
    try:
        os.mkdir(project_path)
        print(f"Created project directory: {project_path}")
    except FileExistsError:
        print(f"Project directory '{project_path}' already exists.")

    # Create subdirectories within the main project directory
    for folder in base_folders:
        folder_path = os.path.join(project_path, folder)
        try:
            os.mkdir(folder_path)
            print(f"Created folder: {folder_path}")
        except FileExistsError:
            print(f"Folder '{folder_path}' already exists.")

    # Handle optional parameters to create additional folders or files
    for param in args:
        param_path = os.path.join(project_path, param)
        try:
            os.mkdir(param_path)
            print(f"Created additional folder: {param_path}")
        except FileExistsError:
            print(f"Additional folder '{param_path}' already exists.")


def main():
    if len(sys.argv) < 2:
        print("Usage: python create_project.py <project_name> [additional_folders...]")
        sys.exit(1)

    project_name = sys.argv[1]
    additional_folders = sys.argv[2:]

    create_project_structure(project_name, *additional_folders)


if __name__ == "__main__":
    main()
