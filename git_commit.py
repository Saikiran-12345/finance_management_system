import os
import subprocess

def run_git(cmd):
    print(f"Running: {cmd}")
    subprocess.run(cmd, shell=True, check=True)

def make_commits():
    # Initialize
    if not os.path.exists(".git"):
        run_git("git init")
        
    # Commit 1
    run_git("git add manage.py config/ requirements.txt .gitignore README.md scaffold.py count_loc.py")
    run_git('git commit -m "Initial commit: Project structure and Django configuration"')
    
    # Commit 2
    run_git("git add users/")
    run_git('git commit -m "feat: Authentication and User management modules"')
    
    # Commit 3
    run_git("git add accounts/")
    run_git('git commit -m "feat: Account management models and views"')
    
    # Commit 4
    run_git("git add income/ expenses/")
    run_git('git commit -m "feat: Income and Expense tracking system"')
    
    # Commit 5
    run_git("git add transactions/")
    run_git('git commit -m "feat: Transaction ledger and core tracking logic"')
    
    # Commit 6
    run_git("git add budgets/ savings/")
    run_git('git commit -m "feat: Budget planning and Savings goals features"')
    
    # Commit 7
    run_git("git add ml/ analytics/ data/")
    run_git('git commit -m "feat: Advanced Machine Learning insights and models"')
    
    # Commit 8
    run_git("git add core/")
    run_git('git commit -m "feat: Enterprise integrations, Tax engine, and core services"')
    
    # Commit 9
    run_git("git add templates/ static/ sdks/")
    run_git('git commit -m "feat: Frontend UI templates, Javascript SDK, and Custom CSS framework"')
    
    # Commit 10
    run_git("git add .")
    run_git('git commit -m "chore: Finalise APIs, Reports, Testing suite, and documentation"')

    print("Successfully created 10 meaningful commits.")

if __name__ == "__main__":
    make_commits()
