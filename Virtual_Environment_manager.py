import os
import subprocess
import sys

def create_virtual_env(project_name):
    """
    Creates a virtual environment for the project.
    """
    venv_path = os.path.join(project_name, 'venv')
    if not os.path.exists(venv_path):
        subprocess.run([sys.executable, '-m', 'venv', venv_path])
        print(f"Virtual environment created at: {venv_path}")
    else:
        print("Virtual environment already exists.")

def activate_virtual_env(project_name):
    """
    Activates the virtual environment.
    """
    venv_path = os.path.join(project_name, 'venv')
    if os.name == 'nt':  # Windows
        activate_script = os.path.join(venv_path, 'Scripts', 'activate.bat')
    else:  # Unix or MacOS
        activate_script = os.path.join(venv_path, 'bin', 'activate')
    
    if os.path.exists(activate_script):
        print(f"To activate the virtual environment, run:\nsource {activate_script}")
    else:
        print("Virtual environment activation script not found. Ensure the virtual environment was created properly.")

def install_requirements(project_name):
    """
    Installs packages from the requirements.txt file.
    """
    venv_path = os.path.join(project_name, 'venv')
    requirements_path = os.path.join(project_name, 'requirements.txt')
    
    if os.path.exists(requirements_path):
        pip_executable = os.path.join(venv_path, 'Scripts', 'pip') if os.name == 'nt' else os.path.join(venv_path, 'bin', 'pip')
        subprocess.run([pip_executable, 'install', '-r', requirements_path])
        print(f"Packages from {requirements_path} installed successfully.")
    else:
        print("requirements.txt file not found. Skipping package installation.")

def main():
    project_name = input("Enter your project name: ")
    
    create_virtual_env(project_name)
    activate_virtual_env(project_name)
    
    install_choice = input("Do you want to install packages from requirements.txt? (y/n): ")
    if install_choice.lower() == 'y':
        install_requirements(project_name)
    
if __name__ == "__main__":
    main()
