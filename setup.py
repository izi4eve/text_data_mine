"""
All requirements are described in requirements.txt.
Run `python setup.py` in terminal to install all requirements.
"""

import os
import subprocess
import sys

def install_requirements():
    req_file = os.path.join(os.path.dirname(__file__), 'requirements.txt')
    if not os.path.exists(req_file):
        print("requirements.txt not found. Please create it.")
        sys.exit(1)
    
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", req_file])
        print("All dependencies installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to install dependencies: {e}")
        sys.exit(1)

if __name__ == "__main__":
    install_requirements()