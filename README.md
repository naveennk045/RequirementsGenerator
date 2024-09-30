# Python Requirements Generator

This Python script helps you generate a `requirements.txt` file based on the imported modules in your Python files, making it easier to manage your project dependencies.

## Features
- Automatically scans a specified folder for Python files (`.py`).
- Generates a `requirements.txt` file using the `pipreqs` module.
- Ignores unnecessary folders such as virtual environments (`env/Lib/site-packages`).
- Provides clear error handling and informative messages to guide the user.

## Requirements
- Python 3.x
- `pipreqs` module (install with: `pip install pipreqs`)

## Installation
1. Clone the repository or download the script.
2. Install the required module by running:

    ```bash
    pip install pipreqs
    ```

## How to Use
1. Open your terminal or command prompt.
2. Navigate to the folder containing the script.
3. Run the script:
   
    ```bash
    python script_name.py
    ```
4. The script will prompt you for a folder path that contains Python files.
5. Enter the path to the folder containing the `.py` files you want to scan for dependencies.


6.  If the folder contains Python files, the script will use pipreqs to generate a requirements.txt file.

7.  The requirements.txt file will be saved in the same folder where your Python files are located.

### Inputs

  - **Folder Path**: You will need to provide the absolute or relative path to the folder containing Python files (.py).
    
    Example:
    ```bash
    Please enter the folder path containing Python files: /path/to/your/project
    ````
### Outputs
  - The generated requirements.txt file will be created in the specified folder, listing all external libraries imported in your Python scripts.
    Example Usage
    
    ```bash
    $ python script_name.py
    ```

    ````bash
    Please enter the folder path containing Python files: /home/user/myproject
    requirements.txt generated successfully.
    ````
- If the folder doesn't contain any Python files, you will get the following message:

    ```bash
      No Python files found in the specified folder.
    ````
- If the folder path is invalid, you'll see this:

  ```bash
  Invalid folder path. Please try again.
  ````

# The pipreqs Module
## Overview
  pipreqs is a Python tool designed to generate a requirements.txt file based on the actual imports used in a project. Unlike traditional tools like pip freeze that output all installed packages (including development and local environment dependencies), pipreqs scans your Python files and lists only the external libraries that are imported in your code.

## Why Use pipreqs?
- **Targeted Dependency Listing**: Instead of listing all installed packages, pipreqs ensures only the dependencies that your project actually needs are included in the requirements.txt.

- **Excludes Development Dependencies**: It avoids including modules related to development or testing environments, especially those in folders like env/Lib/site-packages.

## Key Features of pipreqs:
- **Customizable**: You can specify which directories to ignore (e.g., env/Lib/site-packages).
- **Simple and Lightweight**: Designed for quick and efficient generation of the requirements.txt file.

- For more details on pipreqs, visit the official documentation: https://pypi.org/project/pipreqs/


## License
  This project is licensed under the MIT License. See the LICENSE file for details.
