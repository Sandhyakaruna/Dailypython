import os

def create_project_structure(project_name):
    """
    Creates a standard project structure for a Python project.
    """
    folders = [
        f"{project_name}/src",
        f"{project_name}/src/{project_name}",
        f"{project_name}/tests",
        f"{project_name}/docs",
        f"{project_name}/venv",
        f"{project_name}/scripts",
        f"{project_name}/data"
    ]
    
    files = [
        f"{project_name}/README.md",
        f"{project_name}/requirements.txt",
        f"{project_name}/setup.py",
        f"{project_name}/src/{project_name}/__init__.py",
        f"{project_name}/tests/__init__.py",
        f"{project_name}/.gitignore"
    ]
    
    # Create directories
    for folder in folders:
        os.makedirs(folder, exist_ok=True)
        print(f"Created folder: {folder}")
    
    
    for file in files:
        with open(file, 'w') as f:
            f.write("")  # Create an empty file
        print(f"Created file: {file}")

    print(f"\nProject structure for '{project_name}' created successfully!")

if __name__ == "__main__":
    project_name = input("Enter your project name: ")
    create_project_structure(project_name)
