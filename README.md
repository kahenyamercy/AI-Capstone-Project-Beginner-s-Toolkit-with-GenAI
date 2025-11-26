### Python Requests Capstone Project – Beginner Friendly

This project shows how to use the Python Requests library to make a simple API call.  
It is written in simple language so beginners can follow easily.

---

### Project Overview

This project demonstrates how to:

- Install and use the Requests library  
- Send a GET request to a real API  
- Receive and print data from the internet  
- Build a small working Python program  

---

### Project Goal

The goal is to create a small program that:

1. Connects to the GitHub API  
2. Retrieves information  
3. Prints the result  

Example output:

{"current_user_url": "https://api.github.com/user
", ...}


---

### What Is the Requests Library?

Requests is a simple Python tool that helps your code:

- Visit websites  
- Fetch information  
- Communicate with APIs  

A real example is a weather app that checks temperatures online.

---

### Requirements

You need:

- Linux (Ubuntu recommended)  
- Python 3  
- pip  
- Internet connection  
- VS Code or any text editor  

---

### Installation and Setup

#### 1. Update your system
-sudo apt update

#### 2. Install Python and pip
-sudo apt install -y python3 python3-pip


#### 3. Install the Requests library
-pip install requests


#### 4. Create your project folder
-mkdir requests-capstone
-cd requests-capstone


#### 5. Create the main program

Create a file named `app.py` and add:

```python
import requests

response = requests.get("https://api.github.com")
print(response.json())

How to Run the Project

Run the command below:

python3 app.py


You should see JSON data printed on the screen.

Project Structure
requests-capstone/
│
├── app.py
├── README.md
└── .gitignore

Troubleshooting
1. Error: No module named 'requests'

Install it again:

pip install requests

2. Python not running

Use:

python3 app.py