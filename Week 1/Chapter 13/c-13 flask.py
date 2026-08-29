import subprocess
import sys
import os

env_name = "myenv"

# Create the virtual environment
subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
# Determine the path to the new pip executable
if sys.platform == "win32":
    pip_path = os.path.join(env_name, "Scripts", "pip.exe")
else:
    pip_path = os.path.join(env_name, "bin", "pip")

# Capture the current system packages
freeze_out = subprocess.check_output([sys.executable, "-m", "pip", "freeze"])

# Install those packages into the new environment
subprocess.run([pip_path, "install", "-r", "/dev/stdin" if sys.platform != "win32" else "CON"], 
               input=freeze_out, check=True)
