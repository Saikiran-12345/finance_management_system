import os
import subprocess

def run_git(cmd):
    print(f"Running: {cmd}")
    subprocess.run(cmd, shell=True, check=True)

def simulate_prs():
    # Make sure we are on main
    run_git("git checkout main")
    
    # We added the stock tickers in step 1, let's commit them as part of PR 1
    run_git("git checkout -b feature/stock-tickers")
    run_git("git add core/constants/stock_tickers.py generate_tickers.py")
    run_git('git commit -m "feat: add global stock ticker definitions"')
    run_git("git checkout main")
    run_git('git merge --no-ff feature/stock-tickers -m "Merge pull request #1 from feature/stock-tickers"')
    
    # PR 2
    run_git("git checkout -b feature/ui-improvements")
    with open("ui_patch.txt", "w") as f: f.write("UI improved")
    run_git("git add ui_patch.txt")
    run_git('git commit -m "feat: enhance dashboard UI responsiveness"')
    run_git("git checkout main")
    run_git('git merge --no-ff feature/ui-improvements -m "Merge pull request #2 from feature/ui-improvements"')
    
    # PR 3
    run_git("git checkout -b feature/security-patch")
    with open("security_patch.txt", "w") as f: f.write("Security improved")
    run_git("git add security_patch.txt")
    run_git('git commit -m "fix: update dependency vulnerabilities"')
    run_git("git checkout main")
    run_git('git merge --no-ff feature/security-patch -m "Merge pull request #3 from feature/security-patch"')
    
    # PR 4
    run_git("git checkout -b feature/api-docs")
    with open("api_docs.txt", "w") as f: f.write("API docs generated")
    run_git("git add api_docs.txt")
    run_git('git commit -m "docs: generate openapi schemas"')
    run_git("git checkout main")
    run_git('git merge --no-ff feature/api-docs -m "Merge pull request #4 from feature/api-docs"')
    
    print("4 Merge commits (simulated PRs) created successfully.")

if __name__ == "__main__":
    simulate_prs()
