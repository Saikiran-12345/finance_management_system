import os

# Apps to add
INSTALLED_APPS_ADDITIONS = """
    'rest_framework',
    'core',
    'users',
    'accounts',
    'income',
    'expenses',
    'transactions',
    'budgets',
    'savings',
    'analytics',
    'notifications',
    'reports',
    'audit',
    'ml',
"""

def update_settings():
    settings_path = os.path.join("config", "settings.py")
    with open(settings_path, "r") as f:
        content = f.read()
    
    # Add installed apps
    content = content.replace(
        "'django.contrib.staticfiles',",
        f"'django.contrib.staticfiles',\n{INSTALLED_APPS_ADDITIONS}"
    )

    # Change AUTH_USER_MODEL
    content += "\nAUTH_USER_MODEL = 'users.User'\n"

    # Add login/logout redirects
    content += "\nLOGIN_URL = 'login'\n"
    content += "LOGIN_REDIRECT_URL = 'dashboard'\n"
    content += "LOGOUT_REDIRECT_URL = 'login'\n"

    # Add templates dir
    content = content.replace(
        "'DIRS': [],",
        "'DIRS': [BASE_DIR / 'templates'],"
    )

    with open(settings_path, "w") as f:
        f.write(content)

if __name__ == "__main__":
    update_settings()
    print("Settings updated.")
