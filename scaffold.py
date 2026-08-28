import os
import subprocess
import sys

def run_cmd(cmd):
    print(f"Running: {cmd}")
    subprocess.run(cmd, shell=True, check=True)

def main():
    # 1. Create requirements.txt
    requirements = """Django>=4.2,<5.0
djangorestframework>=3.14.0
pandas>=2.0.0
numpy>=1.24.0
scikit-learn>=1.2.0
pytest>=7.3.0
pytest-django>=4.5.0
pillow>=10.0.0
"""
    with open("requirements.txt", "w") as f:
        f.write(requirements)
    
    # 2. Setup venv and install dependencies
    if not os.path.exists("venv"):
        run_cmd(f"{sys.executable} -m venv venv")
    
    # 3. Create project
    run_cmd(r"venv\Scripts\python -m pip install -r requirements.txt")
    
    if not os.path.exists("manage.py"):
        run_cmd(r"venv\Scripts\django-admin startproject config .")
    
    # 4. Create apps
    apps = [
        "accounts", "income", "expenses", "transactions", 
        "budgets", "savings", "analytics", "notifications", 
        "reports", "audit", "ml", "users", "core"
    ]
    
    for app in apps:
        if not os.path.exists(app):
            run_cmd(f"venv\Scripts\python manage.py startapp {app}")

    # 5. Create directories
    dirs = [
        "templates",
        "static",
        "static/css",
        "static/js",
        "static/images",
        "data",
        "docs"
    ]
    for d in dirs:
        os.makedirs(d, exist_ok=True)
        with open(os.path.join(d, ".gitkeep"), "w") as f:
            f.write("")

    print("Scaffolding complete.")

if __name__ == "__main__":
    main()
