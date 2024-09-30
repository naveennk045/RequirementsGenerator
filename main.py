import os
import subprocess
import sys

def generate_requirements(folder_path):
    try:
        os.chdir(folder_path)        
        result = subprocess.run(['pipreqs', '--force', '--ignore', 'env/Lib/site-packages', '.'], capture_output=True, text=True)
        if result.returncode == 0:
            print("requirements.txt generated successfully.")
        else:
            print("Failed to generate requirements.txt.")
            print(result.stderr)
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    folder_path = input("Please enter the folder path containing Python files: ").strip()
    if os.path.isdir(folder_path):
        # Check if there are any Python files in the directory
        python_files_exist = any(file.endswith('.py') for file in os.listdir(folder_path))
        if python_files_exist:
            generate_requirements(folder_path)
        else:
            print("No Python files found in the specified folder.")
    else:
        print("Invalid folder path. Please try again.")

if __name__ == "__main__":
    main()
