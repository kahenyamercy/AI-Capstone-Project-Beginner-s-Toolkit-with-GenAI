# Python Requests Capstone Project — Beginner Friendly

Welcome! This tiny capstone project teaches you how to make a real API call using the Python Requests library. It's written for absolute beginners and uses clear, step-by-step instructions so you can get a working program running in minutes.

Badges
- [Beginner-friendly] ![Beginner-friendly](https://img.shields.io/badge/level-beginner-brightgreen)
- [Python] ![Python](https://img.shields.io/badge/language-python-blue)

What you'll learn
- Install and use the requests library
- Send a GET request to a public API (GitHub API)
- Read and print JSON responses
- Build and run a simple Python script

Why this project?
This is a simple, practical way to understand how programs talk to the internet. You’ll see real JSON data, learn how to inspect it, and adapt the code for other APIs (like weather or news).

Prerequisites
- Linux (Ubuntu recommended) or any OS with Python 3
- Python 3.x
- pip (Python package manager)
- Internet connection
- Any text editor (VS Code, Sublime, nano, etc.)

Quickstart — get running in under 5 minutes
1. Update your system (optional)
   sudo apt update

2. Install Python and pip (Ubuntu)
   sudo apt install -y python3 python3-pip

3. Install requests
   pip install requests

4. Create the project folder and file
   mkdir requests-capstone
   cd requests-capstone
   Create a file named `app.py` with the content below.

app.py
```python
import requests

def main():
    response = requests.get("https://api.github.com")
    data = response.json()
    # Pretty-print a couple of useful fields
    print("Current user URL:", data.get("current_user_url"))
    print("API documentation URL:", data.get("documentation_url"))
    # Print full JSON if you want
    # import json; print(json.dumps(data, indent=2))

if __name__ == "__main__":
    main()
```

Run it
python3 app.py

You should see lines like:
Current user URL: https://api.github.com/user
API documentation URL: https://docs.github.com/rest

Project structure
requests-capstone/
├── app.py
├── README.md
└── .gitignore

Troubleshooting
- ModuleNotFoundError: No module named 'requests'  
  -> Run: pip install requests

- Python doesn't run with python:  
  -> Use: python3 app.py

Next steps / ideas
- Modify the script to call another endpoint (e.g., https://api.github.com/repos/{owner}/{repo})
- Parse and display specific fields (stars, forks, description)
- Add command-line arguments to request different endpoints

Contributing
Contributions, questions, and suggestions are welcome. If you want to improve this guide, open a PR or file an issue.

License
MIT — see LICENSE file for details

Contact
Maintainer: kahenyamercy