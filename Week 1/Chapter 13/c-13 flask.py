import subprocess
import sys
import os

env_name = "myenv"


subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
if sys.platform == "win32":
    pip_path = os.path.join(env_name, "Scripts", "pip.exe")
else:
    pip_path = os.path.join(env_name, "bin", "pip")

freeze_out = subprocess.check_output([sys.executable, "-m", "pip", "freeze"])
subprocess.run([pip_path, "install", "-r", "/dev/stdin" if sys.platform != "win32" else "CON"], 
               input=freeze_out, check=True)
