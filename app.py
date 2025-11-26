import requests  # Load the requests library

# Make a GET request to the GitHub API
response = requests.get("https://api.github.com")

# Print the response in JSON format
print(response.json())
