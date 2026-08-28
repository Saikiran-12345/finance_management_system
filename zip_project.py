import os
import zipfile

def zip_project(output_filename):
    print(f"Creating {output_filename}...")
    
    # Exclude these directories
    exclude_dirs = {'venv', '__pycache__', '.idea', '.vscode'}
    
    with zipfile.ZipFile(output_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk('.'):
            # Modify dirs in-place to avoid walking into excluded directories
            dirs[:] = [d for d in dirs if d not in exclude_dirs]
            
            for file in files:
                # Don't zip the zip file itself
                if file == output_filename:
                    continue
                    
                file_path = os.path.join(root, file)
                # Add to zip with relative path
                arcname = os.path.relpath(file_path, '.')
                zipf.write(file_path, arcname)
                
    print(f"Successfully created {output_filename}!")

if __name__ == "__main__":
    zip_project("finance_management_system.zip")
