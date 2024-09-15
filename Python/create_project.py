import os
import shutil
import sys


def create_project(name):
    # Get the current working directory to set the path relative to it
    base_path = os.path.abspath(os.path.join(os.getcwd(), os.pardir))  # Move up one directory from current
    project_path = os.path.join(base_path, name)

    # Define folder names
    folders = ['MATLAB', 'LTSpice', 'KiCad', 'EasyEDA', 'Python', 'Arduino']

    # Create each directory inside the project
    for folder in folders:
        os.makedirs(os.path.join(project_path, folder), exist_ok=True)

    # Source and destination for the library copy
    src_lib_path = os.path.join(base_path, 'Python', 'libraries')
    dest_lib_path = os.path.join(project_path, 'Arduino')

    # Copy the libraries to the Arduino folder
    try:
        if os.path.exists(src_lib_path):
            shutil.copytree(src_lib_path, os.path.join(dest_lib_path, 'libraries'), dirs_exist_ok=True)
            print(f"Copied libraries to: {os.path.join(dest_lib_path, 'libraries')}")
        else:
            print(f"Source library path does not exist: {src_lib_path}")
    except Exception as e:
        print(f"Error while copying libraries: {e}")

    print(f"Project '{name}' created successfully at {project_path}")


if __name__ == "__main__":
    # Check if the project name is provided
    if len(sys.argv) < 2:
        print("Please provide a project name.")
        sys.exit(1)

    # Use the first command-line argument as the project name
    project_name = sys.argv[1]
    create_project(project_name)
